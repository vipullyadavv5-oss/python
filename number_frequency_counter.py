nums = input("Enter numbers separated by spaces: ").split()

frequency = {}

for num in nums:
    num = int(num)

    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Number Frequencies:")

for num in frequency:
    print(num, ":", frequency[num])
