# calculate the cost of painting the following building walls (both interior and exterior)
#you need to accept area and cost of both interior and exterior walls 

interior_area =float(input("Enter the total interior wall "))
exterior_area =float(input("Enter the total exterior wall "))

interior_cost_per_sq_m = float(input("Enter the cost of painting per square meter for interior wall "))
exterior_cost_per_sq_m = float(input("Enter the cost of painting per square meter for exterior wall"))

# calculate the total cost
interior_total_cost = interior_area * interior_cost_per_sq_m
exterior_total_cost = exterior_area * exterior_cost_per_sq_m
total_cost = interior_total_cost + exterior_total_cost

# display
print("cost of painting interior walls ",interior_total_cost)
print("cost of painting interior walls ",exterior_total_cost)
print("total painting cost ",total_cost)