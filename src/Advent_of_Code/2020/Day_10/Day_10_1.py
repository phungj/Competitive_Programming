import os
import itertools

# From: https://stackoverflow.com/a/34562305
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)

    return zip(a, b)

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')
    all_lines[i] = int(all_lines[i])

adapters = [0]
adapters.extend(sorted(all_lines))
adapters.append(adapters[len(adapters) - 1] + 3)

one_jolt_diffs = 0
three_jolt_diffs = 0

for pair in pairwise(adapters):
    diff = pair[1] - pair[0]

    if diff == 3:
        three_jolt_diffs += 1
    elif diff == 1:
        one_jolt_diffs += 1

print(one_jolt_diffs * three_jolt_diffs)


