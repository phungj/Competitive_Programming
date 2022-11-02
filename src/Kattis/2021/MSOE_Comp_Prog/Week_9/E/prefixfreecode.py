from itertools import permutations

params = input().split(" ")
params = [int(param) for param in params]

strings = []

for _ in range(params[0]):
    strings.append(input())

strings = sorted(strings)

target = input()
index = 1
permutations = permutations(strings, r=params[1])
current_perm = ''.join(next(permutations))

while current_perm != target:
    index += 1
    current_perm = ''.join(next(permutations))

print(index % (1E9 + 7))
