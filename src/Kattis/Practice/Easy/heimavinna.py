problems = input().split(";")

count = 0

for problem in problems:
    if "-" in problem:
        split_problem = problem.split("-")

        count += int(split_problem[1]) - int(split_problem[0]) + 1
    else:
        count += 1

print(count)
