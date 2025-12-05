# Part 1
# with open('input.txt', 'r') as input_file:
#     battery_packs = [line.strip() for line in input_file.readlines()]
#     total_joltage = 0

#     for battery_pack in battery_packs:
#         left_max = max(battery_pack[:-1])
#         left_max_index = battery_pack.index(left_max)

#         total_joltage += int(left_max + max(battery_pack[left_max_index + 1:]))

#     print(total_joltage)

# Part 2
# with open('input.txt', 'r') as input_file:
#     battery_packs = [line.strip() for line in input_file.readlines()]
#     total_joltage = 0

#     for battery_pack in battery_packs:
#         left_max = max(battery_pack[:88])
#         left_max_index = battery_pack.index(left_max)

#         print(len(battery_pack[:88]))

#     print(total_joltage)

def find_best_battery(battery_pack, total_joltage, num_batteries):
    if num_batteries == 12:
        return int(total_joltage)
    elif num_batteries + len(battery_pack) == 12:
        return int(total_joltage + battery_pack)
    else:
        return max(find_best_battery(battery_pack[1:], total_joltage + battery_pack[0], num_batteries + 1), find_best_battery(battery_pack[1:], total_joltage, num_batteries))

with open('input.txt.bak2', 'r') as input_file:
    battery_packs = [line.strip() for line in input_file.readlines()]
    total_joltage = 0

    for battery_pack in battery_packs:
        total_joltage += find_best_battery(battery_pack, '', 0)

    print(total_joltage)
