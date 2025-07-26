def count_digits(num):
    count=0
    while(num>0):
        num//=10
        count+=1
    return count

def armstrong_sum(num,digits):
    temp=num
    result=0
    while(temp>0):
        digit = temp % 10
        result += digit ** digits
        temp //= 10
    return result

def is_armstrong(num):
    digits=count_digits(num)
    return num == armstrong_sum(num,digits)
n=int(input("enter a number:"))
if(is_armstrong(n)):
    print(n,"is anamstrong number:")
else:
    print(n,"emter a no is not armstrong:")
