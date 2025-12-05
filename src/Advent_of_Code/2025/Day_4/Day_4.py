def count_paper_neighbors(x, y, map):
    count = 0
    row_count = len(map)
    col_count = len(map[0])

    if y > 0 and x > 0 and map[y - 1][x - 1] == '@':
        count += 1
    
    if y > 0 and map[y - 1][x] == '@':
        count += 1

    if x > 0 and map[y][x - 1] == '@':
        count += 1
    
    if y < row_count - 1 and x < col_count - 1 and map[y + 1][x + 1] == '@':
        count += 1

    if y < row_count - 1 and map[y + 1][x] == '@':
        count += 1

    if x < col_count - 1 and map[y][x + 1] == '@':
        count += 1

    if y < row_count - 1 and x > 0 and map[y + 1][x - 1] == '@':
        count += 1
    
    if y > 0 and x < col_count - 1 and map[y - 1][x + 1] == '@':
        count += 1

    return count

# Part 1
# with open('input.txt', 'r') as input_file:
#     map = [line.strip() for line in input_file.readlines()]

#     free_roll_count = 0

#     for y in range(len(map)):
#         for x in range(len(map[0])):
#             if map[y][x] == '@':
#                 free_roll_count += 1 if count_paper_neighbors(x, y, map) < 4 else 0

#     print(free_roll_count)

with open('input.txt', 'r') as input_file:
    map = [list(line.strip()) for line in input_file.readlines()]

    removed_roll_count = 0
    rolls_removed = True

    while rolls_removed:
        rolls_removed = False

        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == '@' and count_paper_neighbors(x, y, map) < 4:
                    removed_roll_count += 1
                    rolls_removed = True
                    map[y][x] = '.'

    print(removed_roll_count)