def palindrome(num):
    temp=num
    reverse=0
    while(num>0):
        a=num % 10
        reverse=reverse*10+a
        num=num//10
    return temp == reverse
n= int(input("enter  a number:"))
if(palindrome(n)):
    print(n,"is palindrome no:")
else:
    print(n,"no is not palindrome ")
