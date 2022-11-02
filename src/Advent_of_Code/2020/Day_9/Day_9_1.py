import os
from itertools import combinations

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')
    all_lines[i] = int(all_lines[i])

preamble = []

for i in range(25):
    preamble.append(all_lines.pop(0))

valid = False

for num in all_lines:
    for pair in combinations(preamble, r=2):
        if num == sum(pair):
            valid = True

    if valid:
        preamble.pop(0)
        preamble.append(num)
        valid = False
    else:
        print(num)
        break
