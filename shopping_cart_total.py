items = []

n = int(input("Enter number of items: "))

for i in range(n):
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity
    items.append((name, total))

grand_total = 0

for name, total in items:
    print(name, "=", total)
    grand_total += total

print("Grand Total =", grand_total)
