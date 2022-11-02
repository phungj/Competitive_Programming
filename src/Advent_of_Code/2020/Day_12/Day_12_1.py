import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

headings = ["N", "E", "S", "W"]
heading_index = 1
heading = headings[heading_index]
x = 0
y = 0


def heading_handler(current_heading, n):
    global heading, heading_index

    if current_heading == "N":
        return 0, n
    elif current_heading == "S":
        return 0, -int(n)
    elif current_heading == "E":
        return n, 0
    elif current_heading == "W":
        return -int(n), 0
    elif current_heading == "F":
        return heading_handler(heading, n)
    elif current_heading == "L":
        offset = int(n) / 90
        heading_index = heading_index - offset
        heading_index = heading_index + 4 if heading_index < 0 else heading_index
        heading = headings[int(heading_index)]
        return 0, 0
    elif current_heading == "R":
        offset = int(n) / 90
        heading_index = abs(heading_index + offset) % 4
        heading = headings[int(heading_index)]
        return 0, 0


for line in all_lines:
    current_heading = line[0]
    current_n = line[1:]
    x_offset, y_offset = heading_handler(current_heading, current_n)
    x += int(x_offset)
    y += int(y_offset)

print(abs(x) + abs(y))
