str1 = 'Python'
# op : {'P':'p','Y':'y',...}

dict1 = {}
for i in str1:
    dict1[i.upper()] = i.lower()
print(dict1)

dict2 = {i.upper():i.lower() for i in str1 }
print(dict2)

keys = [1,2,3,4,5]
values = [10,20,30,40,50]

dict0 = {k:v for k,v in zip(keys,values)}
print("dict0 : ",dict0)

dict1 = {}
for i in range(len(keys)):
    for j in range(len(values)):
        if i==j:
            dict1[keys[i]]=values[j]
print("dict1 : ",dict1)

dict2 = {keys[i]:values[j] for i in range(len(keys)) for j in range(len(values)) if i==j}
print("dict2 : ",dict2)

dict3 = {}
for i in range(len(keys)):
    dict3[keys[i]] = values[i]
print("dict3 : ",dict3)

dict4 = {keys[i]:values[i] for i in range(len(keys))}
print("dict4 : ",dict4)