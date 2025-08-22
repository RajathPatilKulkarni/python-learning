from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")

try:
    with open(file_name, "rt") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    counters[char.lower()] += 1

    for char in sorted(counters.keys()):
        if counters[char] > 0:
            print(char, '->', counters[char])

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))