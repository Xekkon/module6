def gallons_to_liters(gallons):
    return gallons * 3.78541

def main():
    while True:
        gallons = float(input("Enter volume in gallons (negative to quit): "))

        if gallons < 0:
            print("Thank you for using the converter. Goodbye!")
            break

        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:} liters")

if __name__ == "__main__":
    main()