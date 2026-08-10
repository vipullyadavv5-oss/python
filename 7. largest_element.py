numbers = map(int, raw_input("Enter numbers separated by space: ").split())

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)
