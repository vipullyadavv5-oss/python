text1 = input("Enter first word: ").lower()
text2 = input("Enter second word: ").lower()

if sorted(text1) == sorted(text2):
    print("Anagrams")
else:
    print("Not Anagrams")
