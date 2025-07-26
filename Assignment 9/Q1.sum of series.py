def fact(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*fact(num=1)
    
def sum(num):
    if(num==1):
        return fact(1)
    return fact(num)+sum(num-1)
num=int(input("enter a number :"))
result=sum(num)
print("sum of series 1!+2!+3!+..........n is:",result)
    
    
    