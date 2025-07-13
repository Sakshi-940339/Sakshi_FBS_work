import math

radius=20
length=50
breadth=40
cost_per_meter=35
wire_layers=5

if radius >0 and length>0 and breadth >0 and cost_per_meter > 0 and wire_layers >0:
    semicircle_perimeter = math.pi *radius

    ractangle_perimeter = length +2*breadth

    total_length= semicircle_perimeter + ractangle_perimeter
    total_wire_length=total_length*wire_layers
    total_cost = total_wire_length *cost_per_meter

    print("total wire required :")
    print("total cost of fencing:Rs")

else:
     print("invalid input ! all value must be positive number")