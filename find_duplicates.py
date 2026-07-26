numbers = [1, 2, 3, 2, 4, 5, 1, 6]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicates:", duplicates)
