class Book:
    def __init__(self,bid=0,bname="NA",price=0.0,author="Unkonown"):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

        print("Book object created")

    def __del__(self):
        print("Book object Destroyed ")

    def showBook(self):
        print(f"Book ID:{self.bid},Name:{self.bname},price:{self.price},author:{self.author}")

print("\n---using default cunstructor -----")

b1=Book()
b1.showBook()

print("\n ----- using parameterized constructor -----")
b2=Book(101,"python programming ",499,99,"guido van rassum")
b2.showBook()