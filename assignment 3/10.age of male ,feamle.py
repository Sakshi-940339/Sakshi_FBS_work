gender = input("Enter gender male\female :")
age = int(input("enter age"))

if gender == "male"and age>=21:
    print("you are eligible to marry:")
elif gender == "female" and age>= 18:
    print("you are eligible to marry")
else:
    print("you are not eligible to marry")