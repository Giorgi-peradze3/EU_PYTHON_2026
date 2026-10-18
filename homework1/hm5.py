def count_word_frequencies(string_list):

    all_words = []
    for text in string_list:

        words = text.lower().split()
        all_words.extend(words)

    unique_words = set(all_words)


    frequencies = {}
    for word in unique_words:
        frequencies[word] = all_words.count(word)

    return frequencies



sentences = [
    "Python is great and Python is easy",
    "Learning Python is fun and rewarding",
    "Data science and Python go hand in hand"
]

word_counts = count_word_frequencies(sentences)

print("Unique Words & Frequencies:")
for word, count in word_counts.items():
    print(f"'{word}': {count}")