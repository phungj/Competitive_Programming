import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

row_lower_range = 0
row_upper_range = 127
col_lower_range = 0
col_upper_range = 7

for i in range(len(all_lines)):
    for char in all_lines[i]:
        row_new_val = int(row_upper_range / 2)

        if char == 'F':
            row_upper_range = row_new_val
        elif char == 'B':
            row_lower_range = round(row_new_val)
            # TODO: Keep going with the binary search, add a var to track the difference required ot be subtracted from the bounds