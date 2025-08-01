text = input("Enter the text: ")
text = text.lower()
text = "".join(text.split())
if text and text == text[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
