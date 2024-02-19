lst = [2,3,4,5,6,7,8,9,10]
from functools import reduce

# map 

def squre(lst):
    return lst ** 2

map_lst = list(map(squre,lst))
print("Using normal map : ",map_lst)

filter

def even(lst):
    return lst % 2 ==0

filter_lst = list(filter(even,lst))
print("Using normal filter : ",filter_lst)

reduce

def sum(lst,i):
    return lst + i

sum_lst = reduce(sum,lst)
print("Using normal reduce : ",sum_lst)

# lambda

sum = lambda a,b:a+b
print(sum(10,20))

str1 = 'Dipak'

data = lambda a:"Yes string starts with 'D'" if a.startswith('D') else "No string doesn't starts with 'D'"
print(data(str1))

# filter lambda

even_lst = list(filter(lambda lst:lst%2==0,lst))
print("Using filter lambda : ",even_lst)

# map lambda

sq_lst = list(map(lambda lst:lst**2,lst))
print("Using map lambda : ",sq_lst)

# reduce lambda

sum_lst = reduce(lambda lst,i:lst+i,lst)
print("Using reduce lambda : ",sum_lst)

lst = [4,5,6,8,9]

# output : ['even','odd','even','even','odd']

data = list(map(lambda i:'even' if i%2==0 else 'odd',lst))

print(data)

lst = [12,15,17,30,22,25]

data = list(filter(lambda lst : lst%3==0 and lst%5==0,lst))

print(data)

lst = ['apple','mango','banana']

data = list(map(lambda lst : lst[::-1],lst))

print(data)

num = int(input("Enter number : "))
num1 = str(num)
# output = Four Three Five
dict1 = {}
for i in num1:
    if i=='1':
        dict1[i]='One'
    elif i=='2':
        dict1[i]='Two'
    elif i=='3':
        dict1[i]='Three'
    elif i=='4':
        dict1[i]='Four'
    elif i=='5':
        dict1[i]='Five'
    elif i=='6':
        dict1[i]='Six'
    elif i=='7':
        dict1[i]='Seven'
    elif i=='8':
        dict1[i]='Eight'
    elif i=='9':
        dict1[i]='Nine'
    elif i=='0':
        dict1[i]='Zero'
print(dict1)

dict2 = {'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','0':'Zero'}
lst = []
for i in num1:
    if i in dict2.keys():
        lst.append(dict2[i])
print(lst)

lst1 = [dict2[i] for i in num1 if i in dict2.keys()]
# print(lst1)
for i in lst1:
    print(i,end='')
    if i!=lst1[-1]:
        print(end=', ')
print()