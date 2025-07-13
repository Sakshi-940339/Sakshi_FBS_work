num= int(input("enter a three digit no"))

if(100<=num<=999):
   first=num//100
   second=(num//10)%10
   third = num%10
   if first==2*second and first==third/2:
        print("yes you have done :")
   else:
        print("please try next time :")

else:
   print("please enter a valid digit")