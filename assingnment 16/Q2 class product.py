class Product:
    dicount=0

    def __init__(self,pid=None,pname=None,price=0.0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        print("product object created!")

    def __del__(self):
        print(f"Product object with ID {self.pid} is destroyed;")
    
    def ShowBook(self):
        
        print("----------product details--------")
        print(f"product ID:{self.pid}")
        print(f"product Name:{self.pname}")
        print(f"price:{self.price}")
        print(f"Quantity:{self.quantity}")
        print(f"Discount:{Product.discount} %")
        print(f"final price:{self.get_discounted_price()}")

        print("-------")

    def get_discounted_price(self):
        return self.price-(self.price * Product.discount / 100)
    
p1=Product(101,"Laptop",50000,2)

Product.discount=10
p1.ShowBook()

print("-----------")

p2=Product()
p2.ShowBook()