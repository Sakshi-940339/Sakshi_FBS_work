num=int(input("Enter a 3 digit number :"))
copy=num

a=num%10
num=num//10
b=num%10
reverse=(a*10)+b 
c=num//10
reverse=(reverse*10) + c

if(copy==reverse):
    print("the enter a 3 digit num is palindrom")
else:
    print("the enter a 3 digit num is  not palindrom")
