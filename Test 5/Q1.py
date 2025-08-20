D=[2000 ,500,200,100,50,20,10,5]
amount=int(input("enter a amount:"))
print("minimum notes needed :")
for note in D:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(note ,":",count)

