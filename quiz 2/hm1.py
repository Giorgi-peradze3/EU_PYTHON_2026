string = input("Enter a string: ")
unique_symbols = []

for char in string:
    if char != " ":
        if char not in unique_symbols:
            unique_symbols.append(char)
            print(char)