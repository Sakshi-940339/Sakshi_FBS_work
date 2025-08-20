n=int(input("enter a sum of element:"))
list1=[]
for i in range(n):
    num=int(input(f"eneter a element ,{i+1}:"))
    list1.append(num)
sum=0
for num in list1:
    sum +=num
print("sum of all element in the list :",sum)
    
