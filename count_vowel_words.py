sentence = input("Enter Sentence: ")

words = sentence.split()

count = 0

for word in words:
    if word[0].lower() in "aeiou":
        count += 1

print("Words Starting with Vowel:", count)
