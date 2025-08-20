n=int(input("enter a how many number you want to input:"))

list1=[]
for i in range(n):
    num=int(input(f"enter no {i+1}:"))
    list1.append(num)
even_list=[]
odd_list=[]
for num in list1:
    if (num % 2 ==0):
        even_list.append(num)
    else:
        odd_list.append(num)
print("original list:",list1)
print("even element list :",even_list)
print("odd no list :",odd_list)


