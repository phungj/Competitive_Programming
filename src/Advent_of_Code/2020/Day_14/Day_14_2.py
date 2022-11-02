import os
import itertools

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
        if mask[i] == "1":
            val[i] = "1"
        elif mask[i] == "X":
            val[i] = "X"

    return val


# Source: https://stackoverflow.com/questions/33065023/generate-combinations-from-an-input-in-python
def generate_floating_addresses(address, options):
    address = "".join(address)
    address = address.replace('X', '{}')

    for opts in itertools.product(*options):
        yield address.format(*opts)


memory = []
mask = "000000000000000000000000000000000000"

for line in split_all_lines:
    if line[0] == "mask":
        mask = line[1]
    else:
        address = line[0][4:len(line[0]) - 1]
        address = format(int(address), "036b")
        address = apply_mask(mask, address)
        floating_bit_count = address.count("X")
        combinations = ["01" for i in range(floating_bit_count)]

        for masked_address in generate_floating_addresses(address, combinations):
            dec_address = str(int(str(masked_address), 2))

            if check_dupe_memory(dec_address):
                memory = [(addr, val) for (addr, val) in memory if addr != dec_address]

            memory.append((dec_address, line[1]))

sum = 0

for address in memory:
    sum += int(address[1])

print(sum)