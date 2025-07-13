import random
userid=input("enter a userid:")
pass1=input("enter a password :")

if(userid=="FBS" and pass1=="FBS123"):
    captcha=random.randint(1000,9999)
    print("captcha :",captcha)
    input=int(input("Enter a captcha"))

    if(input==captcha):
       print("sucessfully login:")
    else:
       print("captch failed")
else:
     print("unsucessfully login")

    
