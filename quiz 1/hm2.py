def perfnums(lim):
    perfect_numbers = []
    for num in range(1, lim + 1):
        divisors_sum = 0

        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        if divisors_sum == num:
            perfect_numbers.append(num)

    return perfect_numbers



result = perfnums(1000)
print("from 1 till 1000 perfect:", result)