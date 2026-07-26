start = int(input("Enter Start: "))
end = int(input("Enter End: "))

count = 0

for num in range(start, end + 1):
    if num > 1:
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            count += 1

print("Total Prime Numbers:", count)
