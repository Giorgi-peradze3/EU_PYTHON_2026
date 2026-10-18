def reverse_sublist(lst, start, end):


    if not lst or start < 0 or end >= len(lst) or start >= end:
        return lst


    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst



numbers = [10, 20, 30, 40, 50, 60, 70]
print("Original:", numbers)


reverse_sublist(numbers, 1, 4)
print("Modified:", numbers)