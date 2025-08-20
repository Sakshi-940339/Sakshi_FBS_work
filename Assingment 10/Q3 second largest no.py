list1=[47,87,36,100,90,10]
max=list1[0]
sec_max=0
for i in range(1,len(list1)):
    if(max < list1[i]):
        sec_max=max
        max=list1[i]
    elif(sec_max < list1[i] and list1[i] !=max):
        sec_max = list1[i]
print("second max element is :",sec_max)