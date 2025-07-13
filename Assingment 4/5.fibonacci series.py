num=int(input("enter a number :"))

for i in range(1,num+1):
    a=1
    b=0
    for i in range(1,num+1):
        c=a+b
        print(c)
        a=b
        b=c
       