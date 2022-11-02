import os
from functools import reduce

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

split_buses = all_lines[1].split(",")
buses = [item for item in split_buses if item != "x"]
buses = [int(s) for s in buses]

for i in range(len(buses)):
    current_bus = buses[i]
    buses[i] = current_bus, split_buses.index(str(current_bus))


# Python 3.6
# Source: Rosetta Code
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


m = [[] for i in range(len(buses))]

for i in range(len(m)):
    m[i] = buses[i][0]

x = [[] for i in range(len(buses))]

for i in range(len(x)):
    x[i] = buses[i][0] - buses[i][1]

# t % bus_id == 0
# t + 1 % bus_id == 0 (this is the same as) t % bus_id - 1 == 0
print(chinese_remainder(m, x))
