n=int (input("enter number of empolyee "))
Total_all_employee = 0
for i in range(1,n+1):
    print(f"employee  {i}:")
    basic=float(input("enter a basic salary"))
    if (basic < 20000):
        da = 0.10*basic
        ta = 0.12*basic
        har = 0.15*basic
    else:
        da = 0.15*basic
        ta = 0.18*basic
        hra = 0.20*basic
        Total_salary = basic + da + ta + hra
        Total_all_employee += Total_salary
        print(f"Total salary of {i}={Total_salary:2f}")
        print(f"Total salary of all employee={Total_all_employee:2f}")