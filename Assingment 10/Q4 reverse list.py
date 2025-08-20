n= int(input("enter no of element:"))
list1=[]
for i in range(n):
    num=int(input(f"enter  element ,{i+1}:"))
    list1.append(num)
list1.reverse()
print("reverse list",list1)
