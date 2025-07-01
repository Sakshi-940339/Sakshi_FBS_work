# write a program to find the area and permiter of the following figure(accept the length ,bright and radius from user
length=int(input("Enter the length:"))
bright=int(input("enter the bright:"))
radius =int(input("enter a radius:"))

ractangle_area= length * bright
area_semi_circle =0.5 * 3.14 * radius * radius
radius = 2*radius *radius
total_area = ractangle_area +area_semi_circle

ractangle_perimeter=2*(length+bright)

print("the radius of the area",radius)
print("Area ",ractangle_area)
print("perimeter",ractangle_perimeter)