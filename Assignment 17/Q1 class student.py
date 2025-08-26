class Student:
    def __init__(self,sid,name,age,per):
        self.StudentId=sid
        self.Name=name
        self.Age=age
        self.Percentage=per

    def Accept(self):
        self.StudentId=int(input("enter a student ID:"))

        self.Name=input("enter a name:")
        self.Age=int(input("enter precentage:"))
        self.Percentage=float("enter precentage:")

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinaction"
        elif self.Percentage >= 60:
            return "first class:"
        elif self.Percentage >=50:
            return "second class:"
        elif self.Percentage >=35:
            return "pass"
        else:
            return "fail"
        
    def Display(self):
        print(f"ID:{self.StudentId},Name:{self.Name},Age:{self.Age}",f"percentage:{self.Percentage},Rank:{self.CalculateRank()}")
    
    def __str__(self):
            return f"[{self.StudentId},{self.Name},{self.Age},{self.Percentage},{self.CalculateRank()}]"
    

s1=Student(101,"sakshi",20,82.5)
s1.Display()
print(s1)

s2=Student(0,"",0,0.0)
s2.Accept()
s2.Display()