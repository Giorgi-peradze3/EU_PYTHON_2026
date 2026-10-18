def remove_duplicates(lst):

    return list(dict.fromkeys(lst))


numbers = [1, 2, 2, 3, 4, 1, 5, 3]
print("Original:", numbers)
print("Without duplicates:", remove_duplicates(numbers))