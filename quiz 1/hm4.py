text = input("type text: ")

if text == text[::-1]:
    print(text,'is polindrome')
elif text != text[::-1]:
    print(text,'is not polindrome')