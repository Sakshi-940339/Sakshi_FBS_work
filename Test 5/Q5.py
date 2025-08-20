list1=[1,2,3,4,5]
list2=[6,7,3,5,8]

list3=[]
for i in list1:
    if i not in list3:
        list3.append(i)
for i in list3:
    if i not in list3:
        list3.append(i)
print("union",list3)