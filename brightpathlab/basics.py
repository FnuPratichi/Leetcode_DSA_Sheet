import pandas as pd
import numpy as np
# data = {
#     'device_id' : [101,102,103,104],
#     'pressure' : [10,20,'null',10],
#     'temperature' : [80,90,'null',50],
#     'timestamp' : ['25-08-11 10:00:00', '25-08-11 10:01:01', '25-08-11 10:01:02', '25-08-11 10:01:03']
#     }


# df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)


# df = df.replace('null',np.nan)
# print(df)

# df['pressure'] = pd.to_numeric(df['pressure'])
# df['temperature'] = pd.to_numeric(df['temperature'])
# print(df.dtypes)
# ####################################################
# df['timestamp'] = pd.to_datetime(df['timestamp'],format='%y-%m-%d %H:%M:%S')
# print(df['timestamp'])
# df['date'] = df['timestamp'].dt.date
# print(df['date'])

data1 = [
    {"batch_id": "B001", "drug_id": "D100", "timestamp": "2025-08-10 09:00:00", "measurement": 5.6, "status": "Testing"},
    {"batch_id": "B002", "drug_id": "D101", "timestamp": "2025-08-10 09:05:00", "measurement": 7.2, "status": "Review"},
    {"batch_id": "B003", "drug_id": "D100", "timestamp": "2025-08-10 09:10:00", "measurement": -1, "status": "Testing"},
    {"batch_id": "B004", "drug_id": "D102", "timestamp": "2025-08-10 09:15:00", "measurement": 6.8, "status": "Approved"},
    {"batch_id": "B005", "drug_id": "D101", "timestamp": "2025-08-10 09:20:00", "measurement": 8.1, "status": "Testing"},
    {"batch_id": "B006", "drug_id": "D100", "timestamp": "2025-08-10 09:25:00", "measurement": 4.9, "status": "Testing"},
]

df1= pd.DataFrame(data1)
# remove all non positive measurement

measurement_df = df1['measurement']
positive_measurement_df = []
for m in measurement_df:
    if m >= 0:
        positive_measurement_df.append(m)
    if m<0:
        positive_measurement_df.append(0)
print(positive_measurement_df)

df1['measurement'] = positive_measurement_df
print(df1)

my_dict1 = {'name':'anku',
           'age' : 20,
           'class' : 'Null'}

for keys, values in my_dict1.items():
    if values == "Null":
        print(keys)

my_dict2 = {'city':'pune'}

merge = {}
for key in my_dict1:
    merge[key] = my_dict1[key]
for key in my_dict2:
    merge[key] = my_dict2[key]
print(merge)

my_lsi1 = [10,20,20,30]
largest = my_lsi1[0]
second_largest = 0
for i in range(0,len(my_lsi1)):
    if my_lsi1[i]>largest:
        largest = my_lsi1[i]
print(largest)

for i in range(0,len(my_lsi1)):
    if my_lsi1[i]!=largest and my_lsi1[i] > second_largest:
        second_largest = my_lsi1[i]
print(second_largest)

numbers = 5
factorual = 1
for i in range(1,numbers+1):
    if numbers==0:
        print(1)
    if numbers>0:
        factorual = factorual*i 
print(factorual)


new_dict = {'zge':3,'age':2,'city':10}


sorted_values1 = sorted(new_dict.items(),key=lambda x:-x[1])
print(sorted_values1)

sorted_key2 = sorted(new_dict.items(),key=lambda x:x[1])
print(sorted_key2)

sorted_values3 = sorted(new_dict.items())
print(sorted_values3)

most_freq = sorted(new_dict.items(),key=lambda x:(-x[1],x[0]))
result = most_freq[0][0]
print(result)