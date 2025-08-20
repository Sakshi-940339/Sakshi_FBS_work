n=int(input("enter a list element  :"))
list1=[]
for i in range(n):
    ele=input(f"enter a element {i+1}:")
    list1.append(ele)
print("orignal list",list1)
list1.sort(key=len)

print("list sorted by length of element",list1)
