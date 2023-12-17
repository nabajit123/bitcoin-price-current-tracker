class Calculator:
    def add(self, a, b):
        result = a + b  # Method variable
        return result

calculator = Calculator()
print(calculator.add(2, 3))  # Output: 5


# -----------vs-------
class Calculator:
    def __init__(self, a, b):
        self.a = a  # Instance variable
        self.b = b  # Instance variable

    def add(self):
        self.result = self.a + self.b  # Instance variable
        return self.result

calculator = Calculator(2, 3)
print(calculator.add())  # Output: 5
print(calculator.result)  # Output: 5


"""
The difference between this example and the previous one is that the result variable 
is not stored as an instance variable. It doesn't persist beyond the execution of the 
add method. Once the method finishes executing, the result variable is destroyed and 
cannot be accessed outside of the method.

In contrast, the previous example used self.result, which stored the calculated result 
as an instance variable. This allowed the result to be accessed and retained beyond the 
execution of the method. It could be accessed using calculator.result even after calling the add method.

Therefore, the key difference is the lifetime and scope of the variable. Method variables 
are temporary and exist only within the method, while instance variables persist as long as 
the instance of the class exists.
"""



fc_avc_tag = "RES_FC"
cc_pss_id_list = ""
ppa_rate = 5
start_date = "2023-07-01 23:59:00"
end_date = "2023-07-31 23:59:00"
entity_id = "IN_KA"
pss_id_list = pss_id_list = ['SS01286',
 'SS01285',
 'SS00255',
 'SS00556',
 'SS00321',
 'SS01288',
 'SS00633',
 'SS00402',
 'SS00319',
 'SS00170',
 'SS00224',
 'SS00320',
 'SS00169',
 'SS00239',
 'SS00202',
 'SS00173',
 'SS00214',
 'SS01282',
 'SS00281',
 'SS00455',
 'SS00231',
 'SS00213',
 'SS00267',
 'SS00269',
 'SS00181',
 'SS00002',
 'SS00205',
 'SS00208',
 'SS00209',
 'SS00561',
 'SS00547',
 'SS00546',
 'SS00279',
 'SS00686',
 'SS00182',
 'SS00634',
 'SS00211',
 'SS00013',
 'SS00167',
 'SS00250',
 'SS00003',
 'SS00623',
 'SS01287',
 'SS01046',
 'SS00280',
 'SS00030',
 'SS01493',
 'SS01520',
 'SS02111',
 'SS01050',
 'SS00615',
 'SS01279',
 'SS00595',
 'SS00552',
 'SS01444',
 'SS00283',
 'SS00564',
 'SS00896',
 'SS00326',
 'SS00325',
 'SS01043',
 'SS00401',
 'SS00626',
 'SS00510',
 'SS00395',
 'SS00563',
 'SS00398',
 'SS00396',
 'SS01146',
 'SS01280',
 'SS00690',
 'SS00611',
 'SS00270',
 'SS00399',
 'SS01278',
 'SS00341',
 'SS00622',
 'SS01017',
 'SS01283',
 'SS00543',
 'SS00363',
 'SS00692',
 'SS00268',
 'SS00883',
 'SS00539',
 'SS00710',
 'SS00400',
 'SS01277',
 'SS01254',
 'SS00562',
 'SS01256',
 'SS01257',
 'SS00353',
 'SS01259',
 'SS01341',
 'SS01267',
 'SS01255',
 'SS00590',
 'SS01258',
 'SS00264',
 'SS00392',
 'SS01042',
 'SS00316',
 'SS00419',
 'SS01145',
 'SS00282',
 'SS01044',
 'SS00708',
 'SS00450',
 'SS00560',
 'SS00427',
 'SS00424',
 'SS00364',
 'SS00397',
 'SS00451',
 'SS00617',
 'SS00381',
 'SS00594',
 'SS00685',
 'SS01041',
 'SS00688',
 'SS00430',
 'SS00750',
 'SS00702',
 'SS00217',
 'SS00619',
 'SS01230',
 'SS00333',
 'SS00895',
 'SS01234',
 'SS00343',
 'SS00426',
 'SS01167',
 'SS00629',
 'SS00394',
 'SS00429',
 'SS00540',
 'SS01443',
 'SS00620',
 'SS00621',
 'SS00616',
 'SS00332',
 'SS00593',
 'SS00591',
 'SS00592',
 'SS00425',
 'SS00349',
 'SS00707',
 'SS00318',
 'SS00393',
 'SS00691',
 'SS00335',
 'SS00555',
 'SS00317',
 'SS00694',
 'SS00693',
 'SS00725',
 'SS00553',
 'SS00421',
 'SS01465',
 'SS01475',
 'SS01476',
 'SS01477',
 'SS01478',
 'SS01479',
 'SS01510',
 'SS01514',
 'SS01467',
 'SS01473',
 'SS01474',
 'SS01515',
 'SS01452',
 'SS01449',
 'SS01464',
 'SS01468',
 'SS01451',
 'SS01469',
 'SS01470',
 'SS01471',
 'SS01472',
 'SS01466',
 'SS01614',
 'SS01656',
 'SS02087',
 'SS02086',
 'SS02110',
 'SS02150',
 'SS02256',
 'SS02207']