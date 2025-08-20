n=int(input("enter a maximum no and minimun no :"))
list1=[]
for i in range(n):
    num=int(input(f"enter a max num ,{i+1}:"))
    list1.append(num)
list1 =list(set(list1))
print("list after removing duplication ",list1)