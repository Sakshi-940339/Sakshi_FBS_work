import random
correct_userid="admin"
correct_password="1234"

userid =input("enter a userid :")
password=input("enter a password :")
if (userid == "admin" and password == '1234' ):
    captcha = random.randint(1000,9999)
    print("capthcha code:",captcha)

    entered_captcha=input("enter a captcha code show above")
    if entered_captcha == str(captcha):
       print("login successfully:")
    else:
        print("captcha varification failed :")
else:
    print("invalid userid and password :")
     