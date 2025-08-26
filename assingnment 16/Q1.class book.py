class Book:
    count=0
    def __init__(self,bid=None,bname=None,price=None,author=None):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

        Book.count +=1

    def __del__(self):
        print(f"book object with id {self.bid} is destroyed")

    def ShowBook(self):
        print("Book ID:",self.bid)
        print("Book Name:",self.bname)
        print("price:",self.price)
        print("Author:",self.author)
        print("-"*30)

b1=Book(101,"python programming ",450,"Guido van rossum")
b2=Book(102,"c++ programming",500,"bjarne strustrup")
b3=Book()

b1.ShowBook()
b2.ShowBook()
b3.ShowBook()

print("total object created ",Book.count)

        