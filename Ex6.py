import math

def calculate_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    area_in_square_meters = area / 10000  #<- Converting cm² to m²
    unit_price = price / area_in_square_meters
    return unit_price

diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
price1 = float(input("Enter the price of the first pizza (in euros): "))

diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
price2 = float(input("Enter the price of the second pizza (in euros): "))

unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)

print(f"\nPizza 1 unit price: {unit_price1:} euros per square meter")
print(f"Pizza 2 unit price: {unit_price2:} euros per square meter")

if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money.")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same unit price.")