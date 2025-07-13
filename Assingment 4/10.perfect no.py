num=int(input("enter a number :"))
sum_of_divisors=0
 
for i in range(1,num):
    if (num%i==0):
        sum_of_divisors += i

if(sum_of_divisors == num):
    print("perfect no",num)
else:
    print("not prefect no ",num)
