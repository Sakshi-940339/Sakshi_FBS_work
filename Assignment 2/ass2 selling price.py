# selling price of book on cost price discount

cost_price = float(input("enter the cost prices of the book "))
distance = float(input("enter a distance percentage "))

distance_amount = (cost_price * distance) / 100
selling_price = cost_price - distance_amount

print("selling prise of the book:", selling_price)