from collections import ChainMap
import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))

def CheainMap(combined):
    defaults = {'color': 'red', 'user': 'guest'}
    namespace = combined
    command_line_args = {k: v for k, v in namespace.items() if v is not None}

    combined = ChainMap(command_line_args, defaults)
    print(combined['color'])
    print(combined['user'])

CheainMap(combined={'color': 'input_red', 'user': 'guest'})

def fetch_res_act_fc_avc(
    sid_obj, start_date, end_date, actual_data_tag, attr_tags, di_info_data_dict
):
    """
    Forecast, avc and actual data fetching
    """

    exp_index = pd.date_range(start=start_date, end=end_date, freq="15T")

    fc_nd_avc = sid_obj.get_schedule_data(
        start=start_date, end=end_date, src_tag="PSS_SCH_LDCO"
    )
    fc_nd_avc.index.name = "TIMESTAMP"
    fc_nd_avc = fc_nd_avc[["SCHEDULE_VALUE", "AVC_VALUE"]]

    # FC and AVC data based on src tag.
    # if fc_nd_avc_data_tag == "RES_FC":
    # if avc and fc absent for LDCO then fetch RES FC.
    if fc_nd_avc.SCHEDULE_VALUE.count() < len(
        exp_index
    ) or fc_nd_avc.AVC_VALUE.count() < len(exp_index):
        res_fc_df = sid_obj.get_forecast_data(start=start_date, end=end_date)
        res_fc_df = res_fc_df[["POWER_FC"]]

        res_fc_df.rename(columns={"POWER_FC": "SCHEDULE_VALUE"}, inplace=True)

        ldco_fc_df = fc_nd_avc[["SCHEDULE_VALUE"]]
        ldco_fc_df["SCHEDULE_VALUE"].fillna(res_fc_df["SCHEDULE_VALUE"], inplace=True)

        try:
            # temp_avc = sid_obj.get_pss_pro_avc_data(
            #     start=start_date, end=end_date, fc_date=datetime.now()
            # )
            temp_avc = datagetter_report.ret_pss_pro_avc_mis(
                sid_obj.fss_id, start_date, end_date
            )
            temp_avc = temp_avc.fillna(sid_obj.cap_int)

            if temp_avc[temp_avc.columns[0]].count() == 0:
                temp_avc[temp_avc.columns[0]] = sid_obj.cap_int
            temp_avc = temp_avc[["avc"]]
            temp_avc.index.name = "TIMESTAMP"
            temp_avc = temp_avc
            temp_avc.rename(columns={"avc": "AVC_VALUE"}, inplace=True)

            ldco_avc_df = fc_nd_avc[["AVC_VALUE"]]
            ldco_avc_df["AVC_VALUE"].fillna(temp_avc["AVC_VALUE"], inplace=True)

        except (
            Exception
        ) as e:  # AVC tables are deleted. Only latest year table present.
            logger.info(f"While fetching avc data: {e}")
            temp_avc = pd.DataFrame(
                {"TIMESTAMP": exp_index, "avc": [sid_obj.cap_int] * len(exp_index)}
            )
            temp_avc.set_index("TIMESTAMP", inplace=True)

        # Merging frames.
        fc_nd_avc = pd.merge(ldco_fc_df, ldco_avc_df, on="TIMESTAMP", how="inner")
    else:
        fc_nd_avc.index.name = "TIMESTAMP"
        fc_nd_avc = fc_nd_avc[["SCHEDULE_VALUE", "AVC_VALUE"]]
    #     fc_nd_avc = sid_obj.get_schedule_data(
    #         start=start_date, end=end_date, src_tag=fc_nd_avc_data_tag
    #     )

    # Which Actual data need to fetch based on src tag handle by the entities_sch -> datagetter_sch
    temp_act_df = sid_obj.get_pss_pro_actual_data(
        start_date, end_date, src_tag=actual_data_tag, attr_tags=attr_tags
    )
    # if temp_act_df[temp_act_df.columns[0]].count():
    temp_act_df.index.name = "TIMESTAMP"
    # else:
    # print(temp_act_df)
    #     # logger.error(f"Actual data is not available for {actual_data_tag}")
    #     raise Exception(f"Actual data is not available for {actual_data_tag}")

    final_data_frame = pd.merge(fc_nd_avc, temp_act_df, on="TIMESTAMP", how="inner")

    final_data_frame.rename(
        columns={
            "POWER_FC": "FORECAST",
            "SCHEDULE_VALUE": "FORECAST",
            "AVC_VALUE": "AVC",
            "avc": "AVC",
            "POWER_MW": "ACTUAL",
            "ATTRIBUTE_1": "ACTUAL",
        },
        inplace=True,
    )
    final_data_frame = final_data_frame.round(2)

    # Making all actual value <0 to 0.
    final_data_frame["ACTUAL"] = final_data_frame["ACTUAL"].apply(
        lambda x: 0 if x < 0 else x
    )

    return final_data_frame

band_rule_dict = {
    "IN_KA_V1": {
        "INTRA_STATE": {
            "SOLAR": {
                "b1": [0, 15, 0],
                "b2": [15, 25, 0.5],
                "b3": [25, 35, 1.0],
                "b4": [35, 1.5]
            },
            "WIND": {
                "b1": [0, 15, 0],
                "b2": [15, 25, 0.5],
                "b3": [25, 35, 1.0],
                "b4": [35, 1.5]
            }
        }
    },
    "IN_KA_V2": {
        "INTRA_STATE": {
            "SOLAR": {
                "b1": [0, 10, 0],
                "b2": [10, 20, 0.25],
                "b3": [20, 30, 0.5],
                "b4": [30, 0.75]
            },
            "WIND": {
                "b1": [0, 10, 0],
                "b2": [10, 20, 0.25],
                "b3": [20, 30, 0.5],
                "b4": [30, 0.75]
            },
        }
     },
     "IN_TN": {
        "INTRA_STATE": {
            "SOLAR": {
                "b1": [0, 10, 0],
                "b2": [10, 20, 0.25],
                "b3": [20, 30, 0.5],
                "b4": [30, 1]
            },
            "WIND": {
                "b1": [0, 10, 0],
                "b2": [10, 20, 0.25],
                "b3": [20, 30, 0.5],
                "b4": [30,1]
            },
        }
     },
     "INTER_STATE_V1": {
        "SOLAR": {
            "payable":{
                "b1": [0, 15, 1*PPA],
                "b2": [15, 25, 1.1*PPA],
                "b3": [25, 35, 1.2*PPA],
                "b4": [35, 1.3*PPA]
            },
            "receivable":{
                "b1": [0, 15, 1*PPA],
                "b2": [15, 25, 0.9*PPA],
                "b3": [25, 35, 0.8*PPA],
                "b4": [35, 0.7*PPA]
            }
        },
        "WIND": {
            "payable":{
                        "b1": [0, 15, 1*PPA],
                        "b2": [15, 25, 1.1*PPA],
                        "b3": [25, 35, 1.2*PPA],
                        "b4": [35, 1.3*PPA]
                      },
            "receivable":{
                        "b1": [0, 15, 1*PPA],
                        "b2": [15, 25, 0.9*PPA],
                        "b3": [25, 35, 0.8*PPA],
                        "b4": [35, 0.7*PPA]
            }
                },
            },
            "INTER_STATE_V2": {
                "SOLAR": {
                    "payable":{
                     "b1": [0, 10, 1*PPA],
                     "b2": [10,1*PPA+0.1*NormalRate]
                   },
                   "receivable":{
                     "b1": [0, 5, 1*PPA],
                     "b2": [5, 10, 0.9*PPA],
                     "b3": [10,0*PPA]
                   }
                },
                "WIND": {
                    "payable":{
                     "b1": [0, 10, 1*PPA],
                     "b2": [10,1*PPA+0.1*NormalRate]
                   },
                   "receivable":{
                     "b1": [0, 5, 1*PPA],
                     "b2": [5, 10, 0.9*PPA],
                     "b3": [10,0*PPA]
                   }
                },
            },
            "INTER_STATE_V3": {
                "SOLAR": {
                    "payable":{
                     "b1": [0, 10, 1*PPA],
                     "b2": [10,15,1*PPA+0.1*PPA],
                     "b3": [15,1*PPA+0.5*PPA]
                   },
                   "receivable":{
                     "b1": [0, 10, 1*PPA],
                     "b2": [10, 15, 0.9*PPA],
                     "b3": [15,0*PPA]
                   }
                },
                "WIND": {
                    "payable":{
                        "b1": [0, 15, 0],
                        "b2": [15,20,1*PPA+0.1*PPA],
                        "b3": [20,1*PPA+0.5*PPA]
                   },
                   "receivable":{
                        "b1": [0, 15, 1*PPA],
                        "b2": [15, 20, 0.9*PPA],
                        "b3": [20,0*PPA]
                   }
                },
            },
            "IN_GJ_V1":{
                "INTRA_STATE":{
                    "Solar":{
                        "b1":[0,7,0],
                        "b2":[7,15,0.25],
                        "b3":[15,23,0.5],
                        "b4":[23,0.75]
                    },
                    "Wind":{
                        "b1":[0,12,0],
                        "b2":[12,20,0.25],
                        "b3":[20,28,0.5],
                        "b4":[28,0.75]
                    }
                }
            },
            "IN_MP_B":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    }
                }
            }
            "IN_MP_A":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,10,0],
                        "b2":[10,20,0.5],
                        "b3":[20,30,1],
                        "b4":[30,1.5]
                    },
                    "WIND":{
                        "b1":[0,10,0],
                        "b2":[10,20,0.5],
                        "b3":[20,30,1],
                        "b4":[30,1.5]
                    }
                }
            },
            "IN_MH_V1":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    }
                }
            },
            "IN_PB_V1":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    }
                }
            },
            "IN_HR_V1":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    }
                }
            },
            "IN_TG_V1":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    }
                }
            },
            "IN_AP_V1":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    }
                }
            },
            "IN_RJ_V1":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.5],
                        "b3":[25,35,1],
                        "b4":[35,1.5]
                    }
                },
                "INTER_STATE":{
                    "SOLAR": {
                        "payable":{
                         "b1": [0, 15, 1*PPA],
                         "b2": [15, 25, 1.1*PPA],
                         "b3": [25, 35, 1.2*PPA],
                         "b4": [35, 1.3*PPA]
                       },
                       "receivable":{
                         "b1": [0, 15, 1*PPA],
                         "b2": [15, 25, 0.9*PPA],
                         "b3": [25, 35, 0.8*PPA],
                         "b4": [35, 0.7*PPA]
                       }
                    }
                }
            },
            "IN_UP_V1":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.1*PPA],
                        "b3":[25,35,0.2*PPA],
                        "b4":[35,0.3*PPA]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.1*PPA],
                        "b3":[25,35,0.2*PPA],
                        "b4":[35,0.3*PPA]
                    }
                },
                "INTER_STATE":{
                    "SOLAR": {
                        "payable":{
                         "b1": [0, 15, 1*PPA],
                         "b2": [15, 25, 1.1*PPA],
                         "b3": [25, 35, 1.2*PPA],
                         "b4": [35, 1.3*PPA]
                       },
                       "receivable":{
                         "b1": [0, 15, 1*PPA],
                         "b2": [15, 25, 0.9*PPA],
                         "b3": [25, 35, 0.8*PPA],
                         "b4": [35, 0.7*PPA]
                       }
                    }
                }
            },
            "IN_UP_V2":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.1*PPA],
                        "b3":[25,35,0.2*PPA],
                        "b4":[35,0.3*PPA]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.1*PPA],
                        "b3":[25,35,0.2*PPA],
                        "b4":[35,0.3*PPA]
                    },
                "INTER_STATE":{
                    "SOLAR": {
                        "payable":{
                            "b1": [0, 10, 1*PPA],
                            "b2": [10,1*PPA+0.1*NormalRate]
                        },
                        "receivable":{
                            "b1": [0, 5, 1*PPA],
                            "b2": [5, 10, 0.9*PPA],
                            "b3": [10, 0*PPA]
                        }
                    }
                }
            },
            "IN_UP_V3":{
                "INTRA_STATE":{
                    "SOLAR":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.1*PPA],
                        "b3":[25,35,0.2*PPA],
                        "b4":[35,0.3*PPA]
                    },
                    "WIND":{
                        "b1":[0,15,0],
                        "b2":[15,25,0.1*PPA],
                        "b3":[25,35,0.2*PPA],
                        "b4":[35,0.3*PPA]
                    },
                "INTER_STATE":{
                    "SOLAR": {
                        "payable":{
                            "b1": [0, 10, 1*PPA],
                            "b2": [10,15,1*PPA+0.1*PPA],
                            "b3": [15,1*PPA+0.5*PPA]
                          },
                          "receivable":{
                            "b1": [0, 10, 1*PPA],
                            "b2": [10, 15, 0.9*PPA],
                            "b3": [15,0*PPA]
                          }
                        },
                    },
                }
            }
        }}
        
