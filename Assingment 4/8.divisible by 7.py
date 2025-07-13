start=int(input("enter a  start number :"))
stop=int(input("enter  stop number: "))
for i in range(start , stop):
    if(i%7==0 and i%5==0):
        print(i)


