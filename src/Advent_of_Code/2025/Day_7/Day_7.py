from collections import defaultdict
import heapq

def count_splits(splitters, start_position):
    count = 0
    tachyons = [start_position]
    explored = set()
    used_splitters = set()

    while tachyons:
        # print(tachyons)

        current_tachyon = heapq.heappop(tachyons)

        if current_tachyon not in explored:
            current_tachyon_col = current_tachyon[1]

            for splitter_row in splitters[current_tachyon_col]:
                if splitter_row > current_tachyon[0]:
                    if (splitter_row, current_tachyon_col) not in used_splitters:
                        heapq.heappush(tachyons, (splitter_row, current_tachyon_col - 1))
                        heapq.heappush(tachyons, (splitter_row, current_tachyon_col + 1))

                        count += 1

                        used_splitters.add((splitter_row, current_tachyon_col))

                    break
            
            explored.add(current_tachyon)

    return count

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

    splitters = defaultdict(list)
    start_position = None

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '^':
                splitters[j].append(i)
            elif c == 'S':
                start_position = (i, j)

    print(count_splits(splitters, start_position))
    