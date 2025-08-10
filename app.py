# # Transaction Individual Data Analysis_Agg_transation
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//aggregated//transaction//country//india//state//andaman-&-nicobar-islands//2018//1.json",'r')
# D = json.load(Data)
# print(D)

#Agg_insurance
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//aggregated//insurance//country//india//state//andaman-&-nicobar-islands//2020//2.json",'r')
# D = json.load(Data)
# print(D)

#Agg_user 
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//aggregated//user//country//india//state//andaman-&-nicobar-islands//2018//1.json",'r')
# D = json.load(Data)
# print(D)

# #map_transaction
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//map//transaction//hover//country//india//state//andaman-&-nicobar-islands//2018//1.json",'r')
# D = json.load(Data)
# print(D)

#map_insurance
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//map//insurance//hover//country//india//state//andaman-&-nicobar-islands//2020//2.json",'r')
# D = json.load(Data)
# print(D)

#map_user
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//map//user//hover//country//india//state//andaman-&-nicobar-islands//2018//1.json",'r')
# D = json.load(Data)
# print(D)

# #top_transaction
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//top//transaction//country//india//state//andaman-&-nicobar-islands//2018//1.json",'r')
# D = json.load(Data)
# print(D)

# # #top_insurance
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//top//insurance//country//india//state//andaman-&-nicobar-islands//2020//2.json",'r')
# D = json.load(Data)
# print(D)

# #top_user
# import json
# Data = open("E://PHONEPE_PROJECT//pulse//data//top//user//country//india//state//andaman-&-nicobar-islands//2018//1.json",'r')
# D = json.load(Data)
# print(D)
#Agg_trans_Json
# D= {'data': {'from': 1727740800000, 'to': 1735344000000,
#              'transactionData': [{'name': 'Merchant payments', 
#                                   'paymentInstruments': [{'type': 'TOTAL', 'count': 655100809, 'amount': 389286175909.0}]}, 
#                                   {'name': 'Peer-to-peer payments', 
#                                    'paymentInstruments': [{'type': 'TOTAL', 'count': 493217788, 'amount': 1361927136312.0}]}, 
#                                    {'name': 'Recharge & bill payments', 
#                                     'paymentInstruments': [{'type': 'TOTAL', 'count': 76043195, 'amount': 57534056540.0}]}, 
#                                     {'name': 'Financial Services', 
#                                      'paymentInstruments': [{'type': 'TOTAL','count': 2352084, 'amount': 847296537.0}]}, 
#                                      {'name': 'Others', 'paymentInstruments': [{'type': 'TOTAL', 'count': 421806, 'amount': 505364108.0}]}]}, 'responseTimestamp': 1739974491270}
# print (D['data']['transactionData'])
#Agg_insurance_json
# D={"data":{"from":1585679400000,"to":1593282600000,
#            "transactionData":[{"name":"Insurance",
#                 "paymentInstruments":[{"type":"TOTAL","count":6,"amount":1360.0}]}]},
#                 "responseTimestamp":1692610808643}
#Agg_user_json
# D={'data': {'aggregated': {'registeredUsers': 6740, 'appOpens': 0}, 
#             'usersByDevice': [{'brand': 'Xiaomi', 'count': 1665,'percentage': 0.2470326409495549}, 
#                               {'brand': 'Samsung', 'count': 1445, 'percentage': 0.21439169139465875}, 
#                               {'brand': 'Vivo', 'count': 982, 'percentage': 0.1456973293768546}, 
#                               {'brand': 'Oppo', 'count': 501, 'percentage': 0.07433234421364986}, 
#                               {'brand': 'OnePlus', 'count': 332, 'percentage': 0.04925816023738872}, 
#                               {'brand': 'Realme', 'count': 316, 'percentage': 0.04688427299703264}, 
#                               {'brand': 'Apple', 'count': 229, 'percentage': 0.03397626112759644}, 
#                               {'brand': 'Motorola', 'count': 226, 'percentage': 0.03353115727002967}, 
#                               {'brand': 'Lenovo', 'count': 202, 'percentage': 0.02997032640949555}, 
#                               {'brand': 'Huawei', 'count': 158, 'percentage': 0.02344213649851632}, 
#                               {'brand': 'Others', 'count': 684, 'percentage': 0.10148367952522255}]}, 
#                               'responseTimestamp': 1630501494543}

#map_transaction
# d={"data":{"hoverDataList":[{"name":"north and middle andaman district","metric":[{"type":"TOTAL","count":442,"amount":931663.0770939873}]},
#                           {"name":"south andaman district","metric":[{"type":"TOTAL","count":5688,"amount":1.256024934366581E7}]},
#                           {"name":"nicobars district","metric":[{"type":"TOTAL","count":528,"amount":1139848.801225994}]}]},"responseTimestamp":1630502910687}

#map_insurance
# D={'data': {'hoverDataList': [{'name': 'south andaman district', 'metric': [{'type': 'TOTAL', 'count': 3, 'amount': 795.0}]}, 
#                               {'name': 'nicobars district', 'metric': [{'type': 'TOTAL', 'count': 3, 'amount': 565.0}]}]}, 'responseTimestamp': 1692610808730}   
 
# #map_user
# D={'data': {'hoverData': {'north and middle district': {'registeredUsers': 632, 'appOpens': 0}, 
#                           'south andaman district': {'registeredUsers': 5846, 'appOpens': 0}, 
#                           'nicobars district': {'registeredUsers': 262, 'appOpens': 0}}}, 'responseTimestamp': 1630502911500}

# #top_transaction
# D={'data': {'states': None, 'districts': [{'entityName': 'south andaman', 
#                                            'metric': {'type': 'TOTAL', 'count': 5688, 'amount': 12560249.343665812}}, 
#                                            {'entityName': 'nicobars', 
#                                             'metric': {'type': 'TOTAL', 'count': 528, 'amount': 1139848.801225994}}, 
#                                             {'entityName': 'north and middle andaman', 
#                                              'metric': {'type': 'TOTAL', 'count': 442, 'amount': 931663.0770939873}}], 
#                                              'pincodes': [{'entityName': '744101', 
#                                              'metric': {'type': 'TOTAL', 'count': 1622, 'amount': 2769297.9039997994}}, 
#                                              {'entityName': '744103', 
#                                               'metric': {'type': 'TOTAL', 'count': 1223, 'amount': 2238041.8716124697}}, 
#                                               {'entityName': '744102', 
#                                                'metric': {'type': 'TOTAL', 'count': 969, 'amount': 3519059.937562449}}, 
#                                                {'entityName': '744105', 
#                                                 'metric': {'type': 'TOTAL', 'count': 685, 'amount': 1298560.9515503529}}, 
#                                                 {'entityName': '744104', 
#                                                  'metric': {'type': 'TOTAL', 'count': 340, 'amount': 1039715.3111450541}}, 
#                                                  {'entityName': '744107', 
#                                                   'metric': {'type': 'TOTAL', 'count': 302, 'amount': 556059.5308556345}}, 
#                                                   {'entityName': '744301', 
#                                                    'metric': {'type': 'TOTAL', 'count': 283, 'amount': 445739.1633851439}}, 
#                                                    {'entityName': '744112', 
#                                                     'metric': {'type': 'TOTAL', 'count': 269, 'amount': 333709.56700413954}}, 
#                                                     {'entityName': '744202', 
#                                                      'metric': {'type': 'TOTAL', 'count': 193, 'amount': 238914.01667155625}}, 
#                                                      {'entityName': '744302', 
#                                                       'metric': {'type': 'TOTAL', 'count': 168, 'amount': 547469.6509380838}}]}, 
#                                                       'responseTimestamp': 1630501486876}

#top_insurance
# D={'data': {'states': None, 'districts': [{'entityName': 'nicobars', 
#                                            'metric': {'type': 'TOTAL', 'count': 3, 'amount': 565.0}}, 
#                                            {'entityName': 'south andaman', 
#                                             'metric': {'type': 'TOTAL', 'count': 3, 'amount': 795.0}}], 
#                                             'pincodes': 
#                                             [{'entityName': '744301', 
#                                               'metric': {'type': 'TOTAL', 'count': 3, 'amount': 565.0}}, 
#                                               {'entityName': '744104', 
#                                                'metric': {'type': 'TOTAL', 'count': 2, 'amount': 513.0}}, 
#                                                {'entityName': '744101', 
#                                                 'metric': {'type': 'TOTAL', 'count': 1, 'amount': 282.0}}]}, 
#                                                 'responseTimestamp': 1692610808830}

#top_user
# D={'data': {'states': None, 'districts': [{'name': 'south andaman', 'registeredUsers': 5846}, 
#                                         {'name': 'north and middle andaman', 'registeredUsers': 632}, 
#                                         {'name': 'nicobars', 'registeredUsers': 262}], 
#                                         'pincodes': 
#                                         [{'name': '744103', 'registeredUsers': 1608}, 
#                                          {'name': '744101', 'registeredUsers': 1108}, 
#                                          {'name': '744105', 'registeredUsers': 1075}, 
#                                          {'name': '744102', 'registeredUsers': 1006}, 
#                                          {'name': '744104', 'registeredUsers': 272}, 
#                                          {'name': '744202', 'registeredUsers': 237}, 
#                                          {'name': '744112', 'registeredUsers': 215}, 
#                                          {'name': '744301', 'registeredUsers': 207}, 
#                                          {'name': '744107', 'registeredUsers': 196}, 
#                                          {'name': '744211', 'registeredUsers': 156}]}, 
#                                          'responseTimestamp': 1630501494546}