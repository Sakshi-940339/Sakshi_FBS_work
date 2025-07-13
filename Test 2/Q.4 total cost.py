height=float(input("enter a hight of wall :"))
width=float(input("enter a width of wall :"))
cost_per_sq = 10

if height > 0 and width > 0:
    area_one_wall=height * width
    total_area = 4* area_one_wall
    total_cost=total_area*cost_per_sq
    print("total cost of painting 4 walls is rs", total_cost)
    
elif height<=0 and width<=0:
    print("Height of width must be greater than 0")
elif height<=0:
    print("Height must be greater than 0")
elif width<=0:
    print("Width must be greater than 0")

else:
    print("Invalid output")

    