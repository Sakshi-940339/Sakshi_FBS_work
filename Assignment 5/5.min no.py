amount=int(input("enter a amount :"))

denomination =[2000,500,200,100,50,20,10,5,2,1]

print("min number of note /coins :")

for note in denomination:
    if (amount >= note):
        count = amount // note 
        amount = amount % note 
        print(f"{note} * {count}")