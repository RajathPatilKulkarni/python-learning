from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")

try:
    # Count letters
    with open(file_name, "rt") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    counters[char.lower()] += 1

    # Filter only letters that actually appear
    nonzero_counts = {ch: cnt for ch, cnt in counters.items() if cnt > 0}

    # Sort by frequency (descending)
    sorted_letters = sorted(nonzero_counts, key=lambda x: nonzero_counts[x], reverse=True)

    # Save results
    with open(file_name + ".hist", "wt") as out:
        for char in sorted_letters:
            out.write(f"{char} -> {nonzero_counts[char]}\n")

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))