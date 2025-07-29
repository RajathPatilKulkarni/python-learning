text = input("Enter your message: ")
while True:
    try:
        shift = int(input("Enter a number between 1 to 25: "))
        if shift not in range(1, 26):
            print("Number is out of range")
        else:
            break
    except ValueError:
        print("Invalid input, please enter an integer")

cipher = ''
for char in text:
    if char.isalpha():
        base: int = ord('A')if char.isupper() else ord('a')
        code = (ord(char) - base + shift) % 26 + base
        cipher += chr(code)
    else:
        cipher += char

print(cipher)

