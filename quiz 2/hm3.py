students = {}

while True:
    name = input("enter student name: ")

    if name == "!":
        break

    score = float(input("enter student score: "))

    if name not in students:
        students[name] = []


    students[name].append(score)

    if students:
        averages = {}
        for name, scores in students.items():
            averages[name] = sum(scores) / len(scores)
            print(f"{name} : {averages[name]}")

        best_one = max(averages, key=averages.get)
        worst_one = min(averages, key=averages.get)

        print(f"best = {best_one}, worst = {worst_one}")
