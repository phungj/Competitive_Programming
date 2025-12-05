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

import functools

@functools.cache
def find_best_battery(battery_pack, total_joltage, num_batteries):
    if num_batteries == 12:
        return int(total_joltage)
    elif num_batteries + len(battery_pack) == 12:
        return int(total_joltage + battery_pack)
    else:
        return max(find_best_battery(battery_pack[1:], total_joltage + battery_pack[0], num_batteries + 1), find_best_battery(battery_pack[1:], total_joltage, num_batteries))

with open('input.txt', 'r') as input_file:
    battery_packs = [line.strip() for line in input_file.readlines()]
    total_joltage = 0

    for i, battery_pack in enumerate(battery_packs):
        print(i)

        total_joltage += find_best_battery(battery_pack, '', 0)

    print(total_joltage)


# Taken from ChatGPT
# import heapq
# from collections import Counter

# def n_largest_in_order_right_bias(arr, n):
#     """
#     Return the n largest elements (multiplicity preserved) from arr,
#     but when selecting instances of the threshold (the smallest value
#     among the selected n), pick its occurrences from the rightmost positions.
#     The returned list preserves original array order among the selected items.
#     """
#     if n <= 0:
#         return []
#     if n >= len(arr):
#         return list(arr)

#     # 1) determine multiset of values we need
#     largest = heapq.nlargest(n, arr)      # multiset of values (not ordered by positions)
#     needed = Counter(largest)            # counts by value
#     threshold = min(largest)             # smallest value in that multiset

#     # 2) pick the rightmost indices for threshold
#     if needed[threshold] > 0:
#         th_positions = [i for i, v in enumerate(arr) if v == threshold]
#         # choose the rightmost `needed[threshold]` indices
#         rightmost_chosen = set(th_positions[-needed[threshold]:])
#     else:
#         rightmost_chosen = set()

#     # 3) scan left-to-right and pick elements:
#     result = []
#     # make a mutable copy so we can decrement counts for non-threshold values
#     needed_nonthreshold = Counter(needed)
#     for i, v in enumerate(arr):
#         if v == threshold:
#             # include only if this exact occurrence (index) was chosen among the rightmost ones
#             if i in rightmost_chosen:
#                 result.append(v)
#                 # consume one threshold occurrence (not strictly necessary since we used positions,
#                 # but keep it consistent)
#                 needed_nonthreshold[v] -= 1
#         else:
#             if needed_nonthreshold[v] > 0:
#                 result.append(v)
#                 needed_nonthreshold[v] -= 1

#         # early exit once we've collected n items
#         if len(result) == n:
#             break

#     return result


# with open('input.txt', 'r') as input_file:
#     battery_packs = [list(line.strip()) for line in input_file.readlines()]
#     total_joltage = 0

#     for battery_pack in battery_packs:
#         left_max = max(battery_pack[:3])
#         left_max_index = battery_pack.index(left_max)

#         total_joltage += int(left_max + ''.join(n_largest_in_order_right_bias(battery_pack[left_max_index + 1:], 11)))
        
#     print(total_joltage)

