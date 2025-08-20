num=list(map(int,input("enter a number separated by space").split()))
result =[x for x in num if x % 2!=0]
print("list after removing even number ",result)