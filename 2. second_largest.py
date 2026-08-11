nums = map(int, raw_input("Enter numbers: ").split())

largest = second = None

for num in nums:
    if largest is None or num > largest:
        second = largest
        largest = num
    elif num != largest and (second is None or num > second):
        second = num

print("Second Largest:", second)
