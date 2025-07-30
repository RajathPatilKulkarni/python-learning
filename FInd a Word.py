word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

start = 0
for ch in word:
    start = strn.find(ch, start)
    if start == -1:
        print("No")
        break
    start += 1
else:
    print("Yes")