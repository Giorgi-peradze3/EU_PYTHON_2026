string = input("Enter a string: ")

duplicates = []

for char in string:

    if char != " ":

        if string.count(char) > 1 and char not in duplicates:
            duplicates.append(char)

print(f"same char count: {len(duplicates)} . duplicates: {duplicates}")