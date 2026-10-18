from collections import Counter


data = {'Math': 81, 'Physics': 83, 'Chemistry': 87, 'english': 99}


counter_data = Counter(data)


sorted_data = counter_data.most_common()

print("Expected output:", sorted_data)