binary = raw_input("Enter binary number: ")

decimal = 0

for digit in binary:
    decimal = decimal * 2 + int(digit)

print("Decimal:", decimal)
