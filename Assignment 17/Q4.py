class Student:

    def __init__(self,sid,name,):
        self.sid=sid
        self.name=name

    def __str__(self):
        return (f"{self.sid},{self.name}")
class Collage:
    def __init__(self,no_of_students):
            self.no_of_students=no_of_students
            self.students=[]

    def AddStudents(self,student):
        if len(self.students) < self.no_of_students :
            self.students.append(student)
        else:
             print("limit reached!")

    def GetStudent(self,sid):
        for s in self.students:
            if s.sid == sid:
                return s
        return None
    def RemoveStudent(self,sid):
        self.students=[s for s in self.students if s.sid !=sid]

    def __str__(self):
        return "\n".join(str(s)for s in self.students) or "no students"
    
c=Collage(2)
s1=Student(1,"sakshi")
s2=Student(2,"rohit")

c.AddStudents(s1)
c.AddStudents(s2)
print(c)

print("get student",c.GetStudent(1))
c.RemoveStudent(1)
print(c)
              
       

    
