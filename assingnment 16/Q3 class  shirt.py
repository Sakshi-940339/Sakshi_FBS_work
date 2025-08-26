class Shirt:
    size_price={"small":1.0,"medium": 1.1,"large":1.2,"xlarge":1.3}

    def __init__(self,sid=0,sname="NA",stype="NA",price=0.0,size="small"):
        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.price=price
        self.size=size.lower()

        if self.size in Shirt.size_price:
            self.price=self.price * Shirt.size_price[self.size]

    def __del__(self):
        print(f"shirt object with id {self.sid} destroyed")

    def ShowBook(self):
        print("Shirt Details:")
        print(f"ID :{self.sid}")
        print(f"Name:{self.stype}")
        print(f"size:{self.size}")
        print(f"price:{self.price}")

s1=Shirt(101,"peter England","formal",1000,"small")
s1.ShowBook()

s2=Shirt(102,"Levis","Casual",1000,"medium")
s2.ShowBook()

s3=Shirt(103,"Allen Solly","Foraml",1000,"large")
s3.ShowBook()

s4=Shirt(104,"zara","Causal",1000,"xlarge")
s4.ShowBook()