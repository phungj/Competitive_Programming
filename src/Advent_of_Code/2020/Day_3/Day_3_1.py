import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')


current_row = 0
width = len(all_lines[0])
current_column = 0
rise = 1
run = 3
tree_count = 0

while current_row < len(all_lines) - 1:
    current_row += rise
    current_column += run
    current_column %= width
    current_line = all_lines[current_row]
    current_char = current_line[current_column]

    if current_char == '#':
        tree_count += 1

print(tree_count)