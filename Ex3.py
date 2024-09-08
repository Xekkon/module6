def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

while True:
    gallons = float(input("Enter volume in gallons (negative to quit): "))

    if gallons < 0:
            print("Thank you for using the converter. Goodbye!")
            break

    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is equal to {liters:} liters")
