fuel_consumption = float(input('16'))
fuel_price = float(input('48'))
distance = float(input('670'))

fuel_cost = round((distance / 100) * fuel_consumption * fuel_price, 2)
print("The cost of travel", fuel_cost, "hrn")
