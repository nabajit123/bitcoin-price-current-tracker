class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        # bubble_ele = self.nums[0]
        for phase in range(len(self.nums)):
            flag = False
            for inner_loop_idx in range(0, len(self.nums)-phase-1):
                if  self.nums[inner_loop_idx] > self.nums[inner_loop_idx+1]:
                    flag = True
                    temp = self.nums[inner_loop_idx+1]
                    self.nums[inner_loop_idx+1] = self.nums[inner_loop_idx]
                    self.nums[inner_loop_idx] = temp
            
            if flag == False:
                break
        return self.nums




# for sts in temp_df.loc[temp_df.ACTUAL == 0].index:
#     ets = sts+timedelta(minutes=45)
#     ops_df = temp_df.loc[(temp_df.index>=pd.to_datetime(sts)) & (temp_df.index<=pd.to_datetime(ets))]
#     if (ops_df.ACTUAL == 0).sum() == 4:
#         temp_df.loc[(temp_df.index>=pd.to_datetime(sts)) & (temp_df.index<=pd.to_datetime(ets)), "FC"] = 0
temp_df = pd.DataFrame({"PSS_NAME": df.Stn_Name.to_list(), "TIMESTAMP":df.Stn_DC_Date.to_list(), "ACTUAL_DATA": np.NaN})
    condition = (temp_df['PSS_NAME'] == df.Stn_Name.to_list()[0]) & (temp_df['TIMESTAMP'] == df["Stn_DC_Date"].iloc[0])
    temp_df.loc[condition, 'ACTUAL_DATA'] = df.loc[(df.Stn_Name == temp_df['PSS_NAME'].iloc[0]) & ( df["Stn_DC_Date"].iloc[0] == temp_df['TIMESTAMP'].iloc[0])]

df.loc[(df.Stn_Name == temp_df['PSS_NAME'].iloc[0]) & ( df["Stn_DC_Date"] == temp_df['TIMESTAMP'].iloc[0])][f"DC{1}"].iloc[0]



time_intervals = pd.date_range(start=start_timestamp, end=end_timestamp, freq='15T')
temp_df = pd.DataFrame({"PSS_NAME": [df.index[0]]*96, "TIMESTAMP": pd.date_range(start=pd.to_datetime(f"{df['Stn_DC_Date'].iloc[0]} 00:00:00"), end=pd.to_datetime(f"{df['Stn_DC_Date'].iloc[0]} 23:45:00"), freq='15T')})



time_intervals = pd.date_range(start=start_timestamp, end=end_timestamp, freq='15T')
temp_df = pd.DataFrame({"PSS_NAME": [df.index[0]]*96, "TIMESTAMP": pd.date_range(start=pd.to_datetime(f"{df['Stn_DC_Date'].iloc[0]} 00:00:00"), end=pd.to_datetime(f"{df['Stn_DC_Date'].iloc[0]} 23:45:00"), freq='15T')})
for tb in range(0,96):
    temp_df.at[0, "ATUAL"] = df.iloc[:1,:]["DC1"].iloc[0]