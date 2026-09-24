count = int(input("how many subjects u have?: "))

scores = []


for i in range(1, count + 1):
    score = float(input("subject {i}: "))
    scores.append(score)


avg = sum(scores) / count


if avg >= 91:
    grade = "A"
elif avg >= 81:
    grade = "B"
elif avg >= 71:
    grade = "C"
elif avg >= 61:
    grade = "D"
elif avg >= 51:
    grade = "E"
else:
    grade = "F"

print(avg)
print(grade)
