from datetime import datetime

birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year

print("Your age is:", current_year - birth_year)
