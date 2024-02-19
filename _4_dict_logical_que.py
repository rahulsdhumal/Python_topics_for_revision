# input 
lst = [4,5,8,9,2,3]
# output
# {4:[4,8,12,16,20,...,40],5:[5,10,15,20,25,...,50],...}

dict1 = {}
for i in lst:
    lst1 = []
    for j in range(1,11):
        lst1.append(i*j)
    dict1[i] = lst1
    
for k,v in dict1.items():
    print(f'{k} : {v}')
print()

dict2 = {i:[i*j for j in range(1,11)] for i in lst}
# print(dict2)

for k,v in dict2.items():
    print(f'{k} : {v}')