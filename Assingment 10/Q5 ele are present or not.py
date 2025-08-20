n=int (input("enter a list of element:"))
list1=[]
for i in range(n):
    num=int(input(f"enetr a element {1+i}:"))
    list1.append(num)
search=int(input("enter a no of search :"))
count=list1.count(search)
if(count>0):
    print(f"it is present {count}:")
else:
     print(f"it is  not present {search}:")