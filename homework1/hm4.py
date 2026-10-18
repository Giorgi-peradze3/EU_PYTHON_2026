def find_pairs_with_sum(lst, target):
    seen = set()
    pairs = set()

    for num in lst:
        complement = target - num
        if complement in seen:

            pair = tuple(sorted((num, complement)))
            pairs.add(pair)
        seen.add(num)

    return list(pairs)



numbers = [2, 4, 3, 5, 7, 8, -1]
target_sum = 7

result = find_pairs_with_sum(numbers, target_sum)
print(f"Pairs that sum to {target_sum}:", result)