import os
import math

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

min_wait = int(all_lines[0])
buses = all_lines[1].split(",")
buses = [item for item in buses if item != "x"]

max_waits = list(range(len(buses)))

for i in range(len(max_waits)):
    current_bus = int(buses[i])
    max_waits[i] = math.ceil(min_wait / current_bus) * current_bus

best_bus_wait = min(max_waits)
best_bus_difference = best_bus_wait - min_wait
best_bus_id = int(buses[max_waits.index(best_bus_wait)])

print(best_bus_id * best_bus_difference)