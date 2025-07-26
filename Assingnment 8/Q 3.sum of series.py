#a
n=5
def series(num):
    total=0
    for i in range(1,num+1):
        total +=i
    return total
num=int(input("enter  a positive integer :"))
result=series(num)
print("the sum of series is",result)

#b
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
        return fact
def sum_factorial(n):
    total=0
    for i in range(1,n+1):
        total+=factorial(i)
    return total
n=int(input("enter a n:"))
print("sum of factorial series is",sum_factorial(n))

#c
def power_series(n):
    total = 0
    for i in range(1,n+1):
        total+=i**i
    return total
n=int(input("enter a no :"))
print("sum of power_series",power_series)



