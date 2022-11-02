import os
from functools import reduce
from itertools import combinations, tee

# From: https://stackoverflow.com/a/34562305
def pairwise(iterable):
    """
    s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = tee(iterable)
    next(b, None)

    return zip(a, b)


def diff(adapters):
    diffs = []

    for pair in pairwise(adapters):
        diffs.append(pair[1] - pair[0])

    return diffs


file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')
    all_lines[i] = int(all_lines[i])

adapters = [0]
adapters.extend(sorted(all_lines))
max_joltage = adapters[len(adapters) - 1] + 3
adapters.append(max_joltage)

print(adapters)
print(diff(adapters))

current_subsequence = []
subsequences = []
current_base_adapter = adapters.pop(0)
current_subsequence.append(current_base_adapter)

