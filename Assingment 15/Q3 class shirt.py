class shirt:
    def __init__(self,sid=None,sname=None,stype=None,price=None,size=None):
        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.price=price
        self.size=size
        print("constructor called....")

    def __def__(self):
        print("destructor called....")

    def ShowBook(self):
        print("----shirt details -----")
        print(f"shirt ID:{self.sid}")
        print(f"shirt Name:{self.sname}")
        print(f"shirt Type:{self.stype}")
        print(f"shirt price:{self.price}")
        print(f"shirt Size:{self.size}")

print("---------------")
s1=shirt()
s1.ShowBook()

s2=shirt(101,"Raymond","Formal",1200,"Large")
s2.ShowBook()