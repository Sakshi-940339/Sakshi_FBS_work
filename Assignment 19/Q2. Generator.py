#1 finacci number for genrator
def fibonacci(limit):
    a,b = 0,1
    while(a <=limit):
        yield a 
        a,b = b,a+b

for num in fibonacci(50):
    print(num,end=" ")


#2.palindrome number 

def palindrome_number():
    n=0
    while True:
        if str (n)==str(n)[::-1]:
            yield n
        n +=1

gen=palindrome_number()
for _ in range(20):
    print(next(gen),end=" ")

#3.custome rang generator

def my_range(start,stop=None,step=2):
    if (stop is None):
        start,stop=0,start
    if step==0:
        raise ValueError("step cannot be 0")
    if step > 0:
        while(start < stop):
            yield start
            start +=step

for num in my_range(2,10,2):
    print(num,end=" ")

print("\n")

for num in my_range(10,2,-2):
    print(num,end=" ")
        
    

