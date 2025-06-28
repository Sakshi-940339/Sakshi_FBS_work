# convert the distance given in feet and inches into meter and centimeter
feet = int(input("Enter a feet"))
inches = int(input("Enter a inches"))

# conversion factors
#1 foot = 0.3048
#1 inches = 0.0254

# convert to meter
total_meter = (feet*0.3048)+ (inches * 0.0254)

#seperate a meter and centimeter 
meter = int(total_meter)
centimeter = (total_meter-meter)*100

print("meter=",meter)
print("centimeter=",centimeter)