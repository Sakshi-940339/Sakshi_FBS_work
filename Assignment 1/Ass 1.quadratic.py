a=int(input("Enter a a"))
b=int(input("Enter a b"))
c=int(input("Enter a c"))
ans = (b*b)-(4*a*c)
ans = ans** 0.5
root1 = (-b+ans)/(2*a)
root2 = (-b- ans)/(2*a)
print("root1",root1)
print("root2",root2)