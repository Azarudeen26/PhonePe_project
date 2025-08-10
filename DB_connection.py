 # Agg_tran analaysis
import os, json
import pandas as pd

path  = r"E:/PHONEPE_PROJECT/pulse/data/aggregated/transaction/country/india/state/"
Agg_state_list = os.listdir(path)
print ("Agg_state_list=",Agg_state_list)

clm = {'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
for i in Agg_state_list:
    p_i = path+i+"/"
    #print('p_i=',p_i)
    Agg_yr = os.listdir(p_i)
    #print('Agg_yr=',Agg_yr)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        #print('p_j=',p_j)
        Agg_yr_list = os.listdir(p_j)
        #print ('Json=',Agg_yr_list)
        for k in Agg_yr_list:
            p_k = p_j+k
            #print('p_k=',p_k)
            Data = open(p_k,'r')
            D = json.load(Data)
            #print(D)
            for z in D['data']['transactionData']:
              Name = z['name']
              count = z['paymentInstruments'][0]['count']
              amount = z['paymentInstruments'][0]['amount']
              clm['Transacion_type'].append(Name)
              clm['Transacion_count'].append(count)
              clm['Transacion_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
Agg_Trans = pd.DataFrame(clm)
print(Agg_Trans)

# Agg_insurance analaysis
import os, json
import pandas as pd

path  = r"E:/PHONEPE_PROJECT/pulse/data/aggregated/insurance/country/india/state/"
Agg_state_list = os.listdir(path)
print ("Agg_state_list=",Agg_state_list)


clm = {'State':[], 'Year':[],'Quater':[],'insurance_type':[], 'insurance_count':[], 'insurance_amount':[]}
for i in Agg_state_list:
    p_i = path+i+"/"
    #print('p_i=',p_i)
    Agg_yr = os.listdir(p_i)
    #print('Agg_yr=',Agg_yr)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        #print('p_j=',p_j)
        Agg_yr_list = os.listdir(p_j)
        #print ('Json=',Agg_yr_list)
        for k in Agg_yr_list:
            p_k = p_j+k
            #print('p_k=',p_k)
            Data = open(p_k,'r')
            D = json.load(Data)
            #print(D)
            for z in D['data']['transactionData']:
              Name = z['name']
              count = z['paymentInstruments'][0]['count']
              amount = z['paymentInstruments'][0]['amount']
              clm['insurance_type'].append(Name)
              clm['insurance_count'].append(count)
              clm['insurance_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
#Succesfully created a dataframe
Agg_insurance = pd.DataFrame(clm)
print(Agg_insurance)

# Agg_user analaysis_number_3
import os, json
import pandas as pd

path  = r"E:/PHONEPE_PROJECT/pulse/data/aggregated/user/country/india/state/"
Agg_state_list = os.listdir(path)
print ("Agg_state_list=",Agg_state_list)


clm = {'States':[], 'Years':[],'Quarter':[],'Brands':[], 'Transaction_count':[], 'Percentage':[]}
for i in Agg_state_list:
    p_i = path+i+"/"
    #print('p_i=',p_i)
    Agg_yr = os.listdir(p_i)
    #print('Agg_yr=',Agg_yr)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        #print('p_j=',p_j)
        Agg_yr_list = os.listdir(p_j)
        #print ('Json=',Agg_yr_list)
        for k in Agg_yr_list:
            p_k = p_j+k
            #print('p_k=',p_k)
            Data = open(p_k,'r')
            D = json.load(Data)
            #print(D)
            try:
                for z in D['data']['usersByDevice']:
                    brands=z['brand']
                    count=z['count']
                    percentage=z['percentage']
                    clm['Brands'].append(brands)
                    clm['Transaction_count'].append(count)
                    clm['Percentage'].append(percentage)
                    clm['States'].append(i)
                    clm['Years'].append(j)
                    clm['Quarter'].append(int(k.strip('.json')))

            except:
                pass
               
#Succesfully created a dataframe
Agg_user = pd.DataFrame(clm)
print(Agg_user)

# map_transantion analaysis_number_4
import os, json
import pandas as pd

path  = r"E:/PHONEPE_PROJECT/pulse/data/map/transaction/hover/country/india/state/"
map_state_list = os.listdir(path)
print ("map_state_list=",map_state_list)


clm ={'States':[], 'Years':[],'Quarter':[],'District':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in map_state_list:
    p_i = path+i+"/"
    #print('p_i=',p_i)
    map_yr = os.listdir(p_i)
    #print('map_yr=',map_yr)
    for j in map_yr:
        p_j = p_i+j+"/"
        #print('p_j=',p_j)
        map_yr_list = os.listdir(p_j)
        #print ('Json=',map_yr_list)
        for k in map_yr_list:
            p_k = p_j+k
            #print('p_k=',p_k)
            Data = open(p_k,'r')
            D = json.load(Data)
            #print(D)
            for z in D['data']['hoverDataList']:
              Name = z['name']
              count = z['metric'][0]['count']
              amount = z['metric'][0]['amount']
              clm['District'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['States'].append(i)
              clm['Years'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
map_trans = pd.DataFrame(clm)
print(map_trans)

# map_insurance analaysis_number_5
import os, json
import pandas as pd

path_5  = r"E:/PHONEPE_PROJECT/pulse/data/map/insurance/hover/country/india/state/"
map_state_list = os.listdir(path_5)
print ("map_state_list=",map_state_list)


clm ={'States':[], 'Years':[],'Quarter':[],'District':[], 'insurance_count':[], 'insurance_amount':[]}

for states in map_state_list:
    states_5 = path_5+states+"/"
    #print('states_5=',states_5)
    map_yr = os.listdir(states_5)
    #print('map_yr=',map_yr)
    for years in map_yr:
        years_5 = states_5+years+"/"
        #print('years_5=',years_5)
        map_yr_list = os.listdir(years_5)
        #print ('Json=',map_yr_list)
        for file in map_yr_list:
            file_5 = years_5+file
            #print('p_k=',p_k)
            Data = open(file_5,'r')
            D = json.load(Data)
            #print(D)
            for z in D['data']['hoverDataList']:
              Name = z['name']
              count = z['metric'][0]['count']
              amount = z['metric'][0]['amount']
              clm['District'].append(Name)
              clm['insurance_count'].append(count)
              clm['insurance_amount'].append(amount)
              clm['States'].append(states)
              clm['Years'].append(years)
              clm['Quarter'].append(int(file.strip('.json')))
#Succesfully created a dataframe
map_insurance = pd.DataFrame(clm)
print(map_insurance)

# map_user analaysis
import os, json
import pandas as pd

path  = r"E:/PHONEPE_PROJECT/pulse/data/map/user/hover/country/india/state/"
map_state_list = os.listdir(path)
print ("map_state_list=",map_state_list)


clm ={"States":[], "Years":[], "Quarter":[], "District":[], "RegisteredUsers":[], "AppOpens":[]}

for state in map_state_list:
    state_path = path + state + "/"
    #print('state_path=',state_path)
    year_list = os.listdir(state_path)
    #print('year_list=',year_list)
    for year in year_list:
        year_path = state_path + year + "/"
        #print('year_path=',year_path)
        file_list = os.listdir(year_path)
        #print('file_list=',file_list)
        for file in file_list:
            file_path = year_path + file
            #print('file_path=',file_path)
            Data = open(file_path,'r')
            D = json.load(Data)
            #print(D)

            for district, value in D["data"]["hoverData"].items():
                clm["States"].append(state)
                clm["Years"].append(int(year))
                clm["District"].append(district)
                clm["RegisteredUsers"].append(value["registeredUsers"])
                clm["AppOpens"].append(value["appOpens"])
                clm["Quarter"].append(int(file.strip(".json")))
#Succesfully created a dataframe
map_user = pd.DataFrame(clm)
print(map_user)

# top_tran analaysis
import os, json
import pandas as pd

path_7  = r"E:/PHONEPE_PROJECT/pulse/data/top/transaction/country/india/state/"
top_state_list = os.listdir(path_7)
print ("top_state_list=",top_state_list)


clm = {"States":[], "Years":[], "Quarter":[], "Pincode":[], "Count":[], "Amount":[]}
for states in top_state_list:
    states_7 = path_7+states+"/"
    #print('state_7=',state_7)
    top_yr = os.listdir(states_7)
    #print('top_yr=',top_yr)
    for years in top_yr:
        years_7 = states_7+years+"/"
        #print('years_7=',years_7)
        top_yr_list = os.listdir(years_7)
        #print ('Json=',top_yr_list)
        for file in top_yr_list:
            file_7 = years_7+file
            #print('p_k=',p_k)
            Data = open(file_7,'r')
            D = json.load(Data)
            #print(D)
            for i in D["data"]["pincodes"]:
                    if i["entityName"] is None:
                        continue  # Skip null pincodes
                    clm["Pincode"].append(i["entityName"])
                    clm["Count"].append(i["metric"]["count"])
                    clm["Amount"].append(i["metric"]["amount"])
                    clm["States"].append(states)
                    clm["Years"].append(int(years))
                    clm["Quarter"].append(int(file.strip(".json")))

#Succesfully created a dataframe
top_Trans = pd.DataFrame(clm)
print(top_Trans)

# top_insurance analaysis
import os, json
import pandas as pd

path_8  = r"E:/PHONEPE_PROJECT/pulse/data/top/insurance/country/india/state/"
top_state_list = os.listdir(path_8)
print ("top_state_list=",top_state_list)


clm = {"States": [], "Years": [], "Quarter": [], "Pincode": [],"Count": [],"Amount": []}
for states in top_state_list:
    states_8 = path_8+states+"/"
    #print('state_8=',state_8)
    top_yr = os.listdir(states_8)
    #print('top_yr=',top_yr)
    for years in top_yr:
        years_8 = states_8+years+"/"
        #print('years_8=',years_8)
        top_yr_list = os.listdir(years_8)
        #print ('Json=',top_yr_list)
        for file in top_yr_list:
            file_8 = years_8+file
            #print('file_8=',file_8)
            Data = open(file_8,'r')
            D = json.load(Data)
            #print(D)
            for i in D["data"]["pincodes"]:
                    if i["entityName"] is None:
                        continue  # Skip null pincodes
                    clm["Pincode"].append(i["entityName"])
                    clm["Count"].append(i["metric"]["count"])
                    clm["Amount"].append(i["metric"]["amount"])
                    clm["States"].append(states)
                    clm["Years"].append(int(years))
                    clm["Quarter"].append(int(file.strip(".json")))

#Succesfully created a dataframe
top_insurance = pd.DataFrame(clm)
print(top_insurance)

# top_user analaysis
import os, json
import pandas as pd

path_9  = r"E:/PHONEPE_PROJECT/pulse/data/top/user/country/india/state/"
top_state_list = os.listdir(path_9)
print ("top_state_list=",top_state_list)


clm = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

for states in top_state_list:
    states_9 = path_9+states+"/"
    #print('states_9=',states_9)
    top_yr = os.listdir(states_9)
    #print('top_yr=',top_yr)
    for years in top_yr:
        years_9 = states_9+years+"/"
        #print('years_9=',years_9)
        top_yr_list = os.listdir(years_9)
        #print ('Json=',top_yr_list)
        for file in top_yr_list:
            file_9 = years_9+file
            #print('file_9=',file_9)
            Data = open(file_9,'r')
            D = json.load(Data)
            #print(D)
            for i in D["data"]["pincodes"]:
                name = i["name"]
                registeredusers = i["registeredUsers"]
                clm["Pincodes"].append(name)
                clm["RegisteredUser"].append(registeredusers)
                clm["States"].append(states)
                clm["Years"].append(years)
                clm["Quarter"].append(int(file.strip(".json")))

#Succesfully created a dataframe
top_user = pd.DataFrame(clm)
print(top_user)





