def sum(num):
    if(num==0):
        return 0
    return num +sum(num-1)
num=int(input("enter  a no:"))
print("sum is :",sum(num))