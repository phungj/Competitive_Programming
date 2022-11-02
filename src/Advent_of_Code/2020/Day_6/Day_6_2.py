import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

current_answers = []
answers = []

for line in all_lines:
    if line == "":
        answers.append(current_answers)
        current_answers = []
    else:
        current_answers.append(list(line))


def intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


sum = 0
new_answer = []

for answer in answers:
    if len(answer) < 2:
        new_answer = answer[0]
    else:
        new_answer = intersection(answer[0], answer[1])

        for i in range(2, len(answer)):
            new_answer = intersection(new_answer, answer[i])

    sum += len(new_answer)

print(sum)
