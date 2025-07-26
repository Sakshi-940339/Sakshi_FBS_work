def count(num):
    if(num!=0):
        return 1+count(num // 10)
    else:
        return 0
def armstrong (num,c):
    if (num==0):
        return 0
    else:
        return(num % 10)**c+armstrong (num//10,c)
num= int(input("enter a no :"))
c=count(num)
ans=armstrong(num,c)

if(ans==num):
    print(num,"is an armstrong no :")
else:
    print(num,"is not armstrong no:")
