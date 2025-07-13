start=int(input("enter a  start number :"))
end=int(input("enter  end number: "))

divisor=int(input("enter the number to divide:"))

for i in range(start , end+1):
    if(i% divisor==0):
        print(i)

