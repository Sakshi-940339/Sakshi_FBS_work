def reverse(num):
    reverse=0
    while(num>0):
        a =num % 10
        reverse =reverse*10+a
        num=num // 10
    return reverse
num=int(input("enter  a number :"))
reverse_num = reverse(num)
print("reverse no ",reverse_num)
