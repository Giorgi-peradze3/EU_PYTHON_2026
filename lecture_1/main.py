from fontTools.misc.cython import returns


# task 1  write a python program to print string with first 2 and last 2 chars out of input text if its more than 2 chars init
# text = input("Please enter string: ")
#
#
# if len(text) < 2:
#     print("Error: The string must have at least 2 characters!")
# else:
#     result = text[:2] + text[-2:]
#     print("Result:", result)


# task 2 write a python program to get string where all occurances of its first char will be changed by $, except first char
# text_2 = input("please enter text: ")
#
# if len(text_2) > 0:
#      first_char = text_2[0]
#
#      restofthestring = text_2[1:]
#
#      modified = restofthestring.replace(first_char, '$')
#
#      result = first_char + modified
#
#      print("result is:", result)

# task 3 write a python program to count numbers of even and odd in array
# sample_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10]
# odd_nums = 0
# even_nums = 0
#
# for num in sample_nums:
#
#     if num % 2 == 0:
#         even_nums += 1
#
#     else:
#         odd_nums += 1
#
#
# print("Total even numbers:", even_nums)
# print("Total odd numbers:", odd_nums)

# task 4 write a python program to print every num from 0 to 6 except 3 and 6
# for num in range(7):
#
#     if num == 3 or num == 6:
#         continue
#     print(num)


# task 5 write the python function takes list of words and return the longest word and lenght of the word

# def longest_word(words):
#   if not words:
#     return None, 0
#
#   longest = max(words, key=len)
#   return longest, len(longest)
#
# words, lenght = longest_word(["hello", "world", "goodbye", "im sleepy"])
# print("longest word:", words)
# print("lenght:", lenght)

# task 6 write a python program thath accept a string and counts the number of digits and letters

# def count_digits_and_letters(text):
#     letters = 0
#     digits = 0
#
#     for c in text:
#         if c.isdigit():
#             digits += 1
#         elif c.isalpha():
#             letters += 1
#
#
#     return letters, digits
#
# user_inp = input("please enter a string: ")
# letters, digits = count_digits_and_letters(user_inp)
# print("letters:", letters)
# print("digits:", digits)

# task 7 write a python program to fint numbers between 100 and 400 (both included) where each digit of number is an even number. the numbers obtain should be printed in a comma_seperated sequence

even_digits = []

for num in range(100, 401):
    if num % 2 == 0:
        even_digits.append(num)

    print(", " + (even_digits))



