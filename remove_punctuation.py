text = input("Enter Text: ")

result = ""

for ch in text:
    if ch.isalnum() or ch == " ":
        result += ch

print("Text Without Punctuation:", result)
