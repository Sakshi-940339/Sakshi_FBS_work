cp=int(input("Enter a cost value :"))
sp=int(input("Enter a selling value :"))

if(sp>cp):
    profit = sp-cp
    print("profit")
elif(cp>sp):
    loss =cp-sp
    print("loss")
else:
    print("no profit,no loss")