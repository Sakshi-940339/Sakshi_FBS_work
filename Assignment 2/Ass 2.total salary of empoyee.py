# write a program to calculate the total salary of employee based on given components
# DA (dearness allowance)=10%
# TA (travel allowance)=12%
# HAR (house rent allowance)=15

basic= int(input("Enter a basic salary of the employee"))

# calculate alloweance
da = 0.10*basic
ta =0.12*basic
har = 0.15*basic

total_salary = basic +da+ta+har
print("\n salary details...")
print("basic salary of the employee is=",round(total_salary,2))