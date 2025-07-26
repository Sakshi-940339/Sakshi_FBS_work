def prime(num):
    if(num<=1):
        return False
    for i in range(2,int(num**0.5)+1):
        if(num %i==0):
            return False
        return True
    
def sum_of_prime(n):
    total = 0
    for i in range(2,n+1):
        if (prime(i)):
                total+=1
    return total
n= int(input("enter a no :"))
print("sum of all prime no from 1 to" ,n ,"is",sum_of_prime(n))
    

    