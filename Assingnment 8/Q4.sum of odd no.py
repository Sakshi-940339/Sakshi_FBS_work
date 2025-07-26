def odd(num):
    sum=0
    for i in range(1,num+1):
        if(i%2!=0):
            sum +=1
            print(i)
    return sum
num=int(input("enter a  number:"))
print("sum of all number ",odd(num))

