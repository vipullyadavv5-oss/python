print("1. Kilometers to meters")
print("2. Meters to centimeters")
print("3. Kilograms to grams")
print("4. Liters to milliliters")

choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print("Result =", value * 1000, "meters")

elif choice == 2:
    print("Result =", value * 100, "centimeters")

elif choice == 3:
    print("Result =", value * 1000, "grams")

elif choice == 4:
    print("Result =", value * 1000, "milliliters")

else:
    print("Invalid choice")
