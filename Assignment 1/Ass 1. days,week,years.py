# write a program to convert days into year ,week and days
days=int (input("enter a no of days"))
years=int (input("enter a no of years "))
weeks=int (input("enter a no of weeks"))
years=days // 365
days= years % 365
weeks= days // 7
days= weeks % 7
print("years",years)
print("weeks",weeks)
print("days",days)