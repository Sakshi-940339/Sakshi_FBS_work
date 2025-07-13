a1=int(input("Enter a first person:"))
a2=int(input("Enter a second person:"))
a3=int(input("Enter a third person:"))
a4=int(input("Enter a fourth person:"))
a5=int(input("Enter a fifth person:"))
amount=int(input("enter a amount:"))
fair=0

if(a1<12):
    fair+= amount-(amount*0.3)
elif (a1>59):
    fair += amount*0.5
else:
    fair+= amount

if(a2<12):
    fair+= amount-(amount*0.3)
elif (a2>59):
    fair+= amount*0.5
else:
    fair+= amount

if(a3<12):
    fair+= amount-(amount*0.3)
elif (a3 > 59):
    fair+= amount*0.5
else:
    fair+= amount

if(a4<12):
    fair += amount-(amount*0.3)
elif (a4>59):
    fair+= amount*0.5
else:
    fair+= amount

if(a5<12):
    fair+= amount-(amount*0.3)
elif (a5>59):
    fair+= amount*0.5
else:
    fair +=amount*0.5
    print("fair")

   






