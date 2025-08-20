n=int(input("enter a maximum no and minimun no :"))
original_list=[]
for i in range(n):
    num=int(input(f"enter a max num ,{i+1}:"))
    original_list.append(num)
duplicate_list = original_list.copy()
print("original list:",original_list)
print("duplicate list:",duplicate_list)

print("both list are same object in memory",original_list is duplicate_list)