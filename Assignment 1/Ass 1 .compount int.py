#write a program to enter P,T,R compound interest
P=int(input("enter a principle of amount:"))
T=int(input("enter a time in year:"))
R=int(input("enter a rate:"))
CI= P*((1+R/100)**T)
print("the compount interest",CI)