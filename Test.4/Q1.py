def factorial(num):
    fact=1
    for i in range(1,num+1):
        if(num==1):
            return 1
        else:
            return num*factorial(num-1)
num=int(input("enter a number :"))
result=factorial(num)
print("The factorial n in given range ",result)