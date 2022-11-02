import os
from copy import deepcopy


def simulate_step(previous_state, seating, adjacencies):
    for r in range(len(seating)):
        for c in range(len(seating[0])):
            if previous_state[r][c] == "L":
                for adjacency in adjacencies:
                    valid = True

                    try:
                        if previous_state[9999 if r + adjacency[0] < 0 else r + adjacency[0]][9999 if c + adjacency[1] < 0 else c + adjacency[1]] == "#":
                            valid = False
                            break
                    except:
                        pass

                if valid:
                    seating[r][c] = "#"

            elif previous_state[r][c] == "#":
                occupied_count = 0

                for adjacency in adjacencies:
                    try:
                        if previous_state[9999 if r + adjacency[0] < 0 else r + adjacency[0]][9999 if c + adjacency[1] < 0 else c + adjacency[1]] == "#":
                            occupied_count += 1
                    except:
                        pass

                if occupied_count >= 4:
                    seating[r][c] = "L"


def check_seating_equality(previous_state, current_state):
    for r in range(len(previous_state)):
        for c in range(len(current_state)):
            if previous_state[r][c] != current_state[r][c]:
                return False

    return True


file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')
    all_lines[i] = list(all_lines[i])

adjacencies = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


previous_state = deepcopy(all_lines)
simulate_step(previous_state, all_lines, adjacencies)

while not check_seating_equality(previous_state, all_lines):
    previous_state = deepcopy(all_lines)
    simulate_step(previous_state, all_lines, adjacencies)

occupied_count = 0

for seat in [seat for row in all_lines for seat in row]:
    if seat == "#":
        occupied_count += 1

print(occupied_count)
