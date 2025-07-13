
correct_userid="admin"
correct_password="1234"

for attempt in range(1,4):
    userid = input("enter user ID :")
    password=input("enter password :")

    if (userid == correct_userid and password == correct_password):
        print("login successful :")
        break
    else:
        print("incorrect credentials :")

        if (attempt == 3):
            print("maximum attempt reached :")