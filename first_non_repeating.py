text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First Non-Repeating Character:", ch)
        break
else:
    print("No unique character found.")