text = raw_input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in frequency:
    print(ch, ":", frequency[ch])
