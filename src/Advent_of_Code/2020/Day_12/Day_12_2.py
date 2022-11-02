import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

headings = ["N", "E", "S", "W"]
heading_index = 1
heading = headings[heading_index]
waypoint_x = 10
waypoint_y = 1
x = 0
y = 0


def heading_handler(current_heading, n):
    global heading, heading_index, waypoint_x, waypoint_y, x, y

    if current_heading == "N":
        waypoint_y += int(n)
    elif current_heading == "S":
        waypoint_y -= int(n)
    elif current_heading == "E":
        waypoint_x += int(n)
    elif current_heading == "W":
        waypoint_x -= int(n)
    elif current_heading == "F":
        x += int(n) * waypoint_x
        y += int(n) * waypoint_y
    elif current_heading == "L":
        offset = int(n) / 90
        offset %= 4

        if offset == 1:
            temp_waypoint_x = waypoint_x
            temp_waypoint_y = waypoint_y
            waypoint_x = -temp_waypoint_y
            waypoint_y = temp_waypoint_x
        elif offset == 2:
            waypoint_x = -waypoint_x
            waypoint_y = -waypoint_y
        elif offset == 3:
            temp_waypoint_x = waypoint_x
            temp_waypoint_y = waypoint_y
            waypoint_x = temp_waypoint_y
            waypoint_y = -temp_waypoint_x
    elif current_heading == "R":
        offset = int(n) / 90
        offset %= 4

        if offset == 3:
            temp_waypoint_x = waypoint_x
            temp_waypoint_y = waypoint_y
            waypoint_x = -temp_waypoint_y
            waypoint_y = temp_waypoint_x
        elif offset == 2:
            waypoint_x = -waypoint_x
            waypoint_y = -waypoint_y
        elif offset == 1:
            temp_waypoint_x = waypoint_x
            temp_waypoint_y = waypoint_y
            waypoint_x = temp_waypoint_y
            waypoint_y = -temp_waypoint_x


for line in all_lines:
    current_heading = line[0]
    current_n = line[1:]
    heading_handler(current_heading, current_n)

print(abs(x) + abs(y))
