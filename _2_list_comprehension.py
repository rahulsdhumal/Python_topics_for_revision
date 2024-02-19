str1 = "Python"

# o/p : ['P','y','t','h','o','n']
new_lst = []
for i in str1:
    new_lst.append(i)

print(new_lst)

new_lst1 = [i for i in str1]

print(new_lst1)
lst = ["apple","mango","Aeroplane","ac","laptop"]
# op : ["apple","Aeroplane"]
new_lst = []
for i in lst:
    if len(i)>4:
        if i[0] == 'a' or i[0]=='A':
            new_lst.append(i)
print(new_lst)


new_lst = [i for i in lst if len(i)>4 if i[0] == 'a' or i[0]=='A']
print(new_lst)

new_lst = [i for i in lst if len(i)>4 and (i[0] == 'a' or i[0]=='A')]
print(new_lst)

lst = [10,4,6,1,7,8,9,11,56]
new_lst = [lst[i] for i in range(len(lst)) if i in [0,2,5,7]]
print(new_lst)

new_lst = [lst[i] for i in range(len(lst)) if i%2!=0]
print(new_lst)

lst1 = [1,2,3,4,5]
lst2 = [4,6,5,8,7]

lst3 = []
for i in lst1:
    for j in lst2:
        if i==j:
            lst3.append(j)
print(lst3)

lst4 = [j for i in lst1 for j in lst2 if i==j]
print(lst4)
