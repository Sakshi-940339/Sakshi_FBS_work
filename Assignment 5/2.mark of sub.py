num_student= int (input("enter a number of student :"))

all_per=[]

for i in range(num_student):
    print("enter a mark of student :")
    total=0
    for j in range(5):
        mark = float(input("enter a mark of student:"))
        total += mark
        per = total / 5
        all_per.append(per)
        print("per of student :")
        
        average = sum(all_per)/num_student
        print("All percentage :")
        for i , per in enumerate(all_per,1):
            print("student: %")
        print("average percentage of all student :")
