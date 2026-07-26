numbers = [1, 2, 3, 4, 5]

k = int(input("Rotate by: "))

k = k % len(numbers)

numbers = numbers[k:] + numbers[:k]

print("Rotated List:", numbers)
