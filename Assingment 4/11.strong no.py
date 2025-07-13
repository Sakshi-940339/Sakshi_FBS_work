sum=0
num=int(input("enter a no :"))
temp=num
while (temp !=0):
    a=temp%10
    fact=1
    for i in range(1,a+1):
        fact*=i
    sum+=fact
    temp=temp//10
if(sum==num):
    print("strong no:")
else:
    print("Not strong no :")