class Student:
    def __init__(self,sid ,name,age,percentage):
        self.sid=sid
        self.name=name
        self.age=age
        self.percentage=percentage

    def CalculateRank(self):
        if self.percentage >=75:
            return "Distinction"
        elif self.percentage >=60:
            return "first class"
        else:
            return "fail"
        
    def __str__(self):
        return f"ID:{self.sid},Name:{self.name},Age:{self.age},percentage:{self.percentage}"
    
class MedicalStudent(Student):
    def __init__(self,sid,name,age,per,specialization,internship_mark):
        super().__init__(sid,name,age,per)
        self.specialization=specialization
        self.internship_mark=internship_mark
    
    def CalculateRank(self):
        overall=(self.percentage * 0.7) + (self.internship_mark * 0.3)
        if overall >=80:
            return "excellent"
        elif overall >=60:
            return "good"
        else:
            return "average"
    def Display(self):
        print(self)
        
    def __str__(self):
        return (f"MedicalStudent [ID:{self.sid},Name:{self.name},Age:{self.age},per:{self.percentage},spec:{self.specialization},"
                   f"Internshi:{self.internship_mark},Rank:{self.CalculateRank}]")

m1=MedicalStudent(101,"sakshi",22,72,"Cardiology",85)
m1.Display()
        


