import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

totalCount = 0

for line in all_lines:
    pwCount = 0
    split_line = line.split(" ")
    indices = split_line[0].split("-")
    firstIndex = int(indices[0])
    secondIndex = int(indices[1])
    atFirstIndex = False
    atSecondIndex = False
    pwChar = split_line[1][0]
    pw = split_line[2]

    if pwChar == pw[firstIndex - 1]:
        atFirstIndex = True

    if pwChar == pw[secondIndex - 1]:
        atSecondIndex = True

    if atFirstIndex ^ atSecondIndex:
        totalCount += 1

print(totalCount)