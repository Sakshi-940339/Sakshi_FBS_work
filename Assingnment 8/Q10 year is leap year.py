def leap_year(year):
    if(year %4==0):
        if(year % 100!=0 or year % 400==0):
            return True
        return False
year = int(input("enter a year :"))
if (leap_year(year)):
    print(year,"is leap year ")
else:
    print(year,"is not leap year")
