import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

split_all_lines = [[] for i in range(len(all_lines))]

for i in range(len(split_all_lines)):
    split_all_lines[i] = all_lines[i].split(" ")
    split_all_lines[i].remove("=")


# Memory tuple: (address, value)
def check_dupe_memory(checked_address):
    for address in memory:
        if address[0] == checked_address:
            return True

    return False


def apply_mask(mask, val):
    mask = list(mask)
    val = list(val)
    for i in range(len(mask)):
        if mask[i] == "0":
            val[i] = "0"
        elif mask[i] == "1":
            val[i] = "1"

    return "".join(val)


memory = []
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

for line in split_all_lines:
    if line[0] == "mask":
        mask = line[1]
    else:
        address = line[0][4:len(line[0]) - 1]

        if check_dupe_memory(address):
            memory = [(addr, val) for (addr, val) in memory if addr != address]

        val = format(int(line[1]), "036b")
        val = apply_mask(mask, val)
        memory.append((address, val))

sum = 0

for address in memory:
    sum += int(address[1], 2)

print(sum)