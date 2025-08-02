from collections import Counter

text1 = input("Enter the first word: ").lower().replace(' ', '')
text2 = input("Enter the second word: ").lower().replace(' ', '')
length = len(text1)
count = 0

if Counter(text1) == Counter(text2):
    print("Anagrams")
else:
    print("Not anagrams")
