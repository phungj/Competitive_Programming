import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')


def count_trees(run, rise):
    current_row = 0
    width = len(all_lines[0])
    current_column = 0
    rise = rise
    run = run
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


count_trees(1, 1)
count_trees(3, 1)
count_trees(5, 1)
count_trees(7, 1)
count_trees(1, 2)

print(50 * 148 * 53 * 64 * 29)