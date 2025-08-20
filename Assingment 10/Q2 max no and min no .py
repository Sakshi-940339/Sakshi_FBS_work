n=int(input("enter a maximum no and minimun no :"))
list1=[]
for i in range(n):
    num=int(input(f"enter a max num ,{i+1}:"))
    list1.append(num)
maximum=max(list1)
minimum=min(list1)
print("maximun no in list:",maximum)
print("minimum no in list :",minimum)