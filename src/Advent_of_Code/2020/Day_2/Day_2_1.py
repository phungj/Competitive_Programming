import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

totalCount = 0

for line in all_lines:
    pwCount = 0
    split_line = line.split(" ")
    range = split_line[0].split("-")
    lower = int(range[0])
    upper = int(range[1])
    pwChar = split_line[1][0]
    pw = split_line[2]

    for char in pw:
        if pwChar == char:
            pwCount += 1

    if not (pwCount > upper or pwCount < lower):
        totalCount += 1

print(totalCount)