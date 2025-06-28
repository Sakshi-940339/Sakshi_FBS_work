# program to find miinimum no of notes for given amount
amount= int(input("Enter a amount"))

# 500
n500 = amount // 500
r_amount= amount % 500

# 200
n200 = r_amount // 200
r_amount = r_amount % 200

#100 
n100 = r_amount //100
r_amount = r_amount % 100 

# 50
n50 = r_amount //50
r_amount = r_amount % 50

#20
n20 = r_amount //20
r_amount = r_amount % 20

#10
n10 = r_amount //10
r_amount = r_amount % 10
print("notes to be paid for amount",amount)
print("the notes are 500 is",n500)
print("the notes are 200 is",n200)
print("the notes are 100 is",n100)
print("the notes are 50 is",n50)
print("the notes are 20 is",n20)
print("the notes are 10 is",n10)


