def sumOfDigit(num):
    if(num==0):
        return 0
    else:
        a=num % 10
        return a+sumOfDigit(num//10)
num=int(input("enter a no:"))
print(sumOfDigit(num))