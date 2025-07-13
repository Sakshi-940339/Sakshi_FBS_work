# a)

import math
n = int(input("enter value of n :"))
sum=0

for i in range(1, n+1):
    sum += math.factorial(i)
    print("sum serise 1! +2!+.........n!",sum)

#b)

n=int(input("enter a value of n:"))
sum = 0
for i in range(1,n+1):
    sum += n**i
print("sum of n + n^2 +......+n^n =",sum)


#c)

n =int(input("enter a number of terms :"))
sum=0
term=1

for i in range(n):
    sum += term
    term *= 2
print("sum of geometric series =",sum)

#d)

a=int(input("enter a value of a :"))
sum =0
for i in range(1,11):
    sum+=(a ** i)/i
print("sum of S = a + a^2/2+........a^10/10 =",sum)

#e)

x= float(input("enter a value of x :"))
n= float(input("enter a number of term :"))
sum = 0
sign =1
for i in range(1,n+1):
    exponent = i 
    denominator = 2*i-1
    term = (x**exponent)/denominator
    sum +=sign * term
    sign *= -1 
print("sum of serise =",sum)