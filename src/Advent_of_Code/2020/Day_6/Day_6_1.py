import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

current_answers = ""
answers = []

for line in all_lines:
    if line == "":
        answers.append(current_answers)
        current_answers = ""
    else:
        current_answers += line

sum = 0
for answer in answers:
    answer = list(answer)
    answer = set(answer)
    sum += len(answer)

print(sum)

