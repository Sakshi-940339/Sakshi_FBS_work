side1=int(input("enter a first side of triangle :"))
side2=int(input("enter a second side of triangle :"))
side3=int(input("enter a third side of triangle :"))

if (side1 + side2>side3 and side2+side3>side1 and side1+side3+side2) :
    if side1 == side2 == side3:
      print("the triangle is equilateral triangle:")
    elif side1==side2 or side2 == side3 or side1==side3 :
      print("the triangle is isosceles triangle :")
    else:
        print("the triangle is scalene triangle")
else:
      print("the given sides do not form valid trianglr :")

 
    
