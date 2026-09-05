expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = raw_input("Enter choice: ")

    if choice == "1":
        name = raw_input("Enter expense name: ")
        amount = float(raw_input("Enter amount: "))

        expenses.append((name, amount))
        print("Expense added.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for name, amount in expenses:
                print(name, ":", amount)

    elif choice == "3":
        total = 0

        for name, amount in expenses:
            total += amount

        print("Total Expenses:", total)

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
