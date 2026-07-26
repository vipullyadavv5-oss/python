numbers = [1, 2, 2, 3, 4, 2, 5, 5]

mode = numbers[0]
maximum = 0

for num in numbers:
    if numbers.count(num) > maximum:
        maximum = numbers.count(num)
        mode = num

print("Mode:", mode)
