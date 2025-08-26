class Student:
    def __init__(self,sid,name,age,per):
        self.sid=sid
        self.name=name
        self.age=age
        self.per=per

    def display(self):
        print(self.sid,self.name,self.age,self.per)

    def calcualte_rank(self):
        if self.per>=35:
            return "pass"
        else:
            "Fail"

    def __str__(self):
        return f"Student:{self.sid},{self.name},{self.age},{self.per}"
    
class EnggStudent(Student):
    def __init__(self,sid,name,age,per,branch,internal):
        super().__init__(sid,name,age,per)
        self.branch=branch
        self.internal=internal

    def display(self):
        super().display()
        print(self.branch,self.internal)

    def calculate_rank(self):
        score=(self.per + self.internal)/2
        if score>=60:
           return "excellent"
        else:
            "Average"

    def __str__(self):
        return f"enggStudent:{self.sid},{self.name},{self.branch},{self.per},{self.internal}"
    
e=EnggStudent(1,"sakshi",21,70,"computer",80)
e.display()
print("Rank:",e.calculate_rank())
print(e)
    


    


