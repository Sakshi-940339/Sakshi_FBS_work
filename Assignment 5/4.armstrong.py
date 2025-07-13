num=int(input("enter a number :"))

sum=0
temp=num
order = len(str(num))

while (temp > 0):
    digit = temp % 10
    sum += digit ** order
    temp //= 10

    if(sum==num):
        print("is an armstrong number ",num)
    else:
        print( "is not an armstrong number ",num)
