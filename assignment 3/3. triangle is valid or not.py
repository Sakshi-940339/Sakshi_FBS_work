#write a program to input angle of triangle and check whether triangle is valid or not
ang1=int(input("enter a angle 1:"))
ang2=int(input("enter a angle 2:"))
ang3=int(input("enter a angle 3:"))

total_sum = ang1+ang2+ang3
if( total_sum==180 and ang1>0 and ang2>0 and ang3>0):
    print("ang is valid :")
else:
    print("ang is not valid")




