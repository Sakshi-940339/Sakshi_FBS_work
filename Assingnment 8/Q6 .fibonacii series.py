def fibonacci(num):
    a=1
    b=1
    print(a,b ,end=" ")
    for i in range(2,num):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
num=int(input("enter a no "))
if(num<=0):
    print("plz enter a positive integer ")
elif(num==1):
    print(1)
else:
   print("fibonacci series",fibonacci (num))