start=int(input("enter a start no :"))
stop=int(input("enter a stop no :"))

for i in range(start,stop+1):
    temp = i
    count = 0
while(temp != 0):
    count += 1
    temp = temp //10
    temp = i
sum= 0
while(temp != 0):
    a = temp % 10
    sum += a ** count
    temp = temp//10
if(sum==i):
    print(i,"yes it is armstrong no :")
  



