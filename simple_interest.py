principal = float(input("Principal Amount: "))
rate = float(input("Rate (%): "))
time = float(input("Time (years): "))

interest = (principal * rate * time) / 100

print("Simple Interest:", interest)
print("Total Amount:", principal + interest)
