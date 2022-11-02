import os
import copy

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

split_all_lines = [[] for i in range(len(all_lines))]

for i in range(len(all_lines)):
    split_all_lines[i] = all_lines[i].split(" ")
    split_all_lines[i].append("False")


# Tuples are (acc, jmp)
def nop(n):
    return 0, 1


def acc(n):
    return int(n), 1


def jmp(n):
    return 0, int(n)


def parse_num(s):
    sign = s[0]
    num_string = s[1:]
    n = int(num_string)

    if sign == "+":
        return n
    else:
        return -n


def op_switch(current_line):
    op = current_line[0]
    n = current_line[1]
    ops = {
        "nop": nop,
        "acc": acc,
        "jmp": jmp
    }

    f = ops.get(op, lambda: "Invalid OP")
    return f(n)


def run_asm(split_all_lines):
    current_line_index = 0
    accumulator = 0
    i = 0

    while current_line_index < len(split_all_lines) and i < 100000:
        current_line = split_all_lines[current_line_index]
        acc_offset, jmp_offset = op_switch(current_line)
        accumulator += acc_offset
        current_line_index += jmp_offset
        i += 1

    if current_line_index >= len(split_all_lines):
        print(accumulator)


for i in range(len(split_all_lines)):
    new_split_all_lines = copy.deepcopy(split_all_lines)
    current_op = split_all_lines[i][0]

    if current_op == "nop":
        new_split_all_lines[i][0] = "jmp"
        run_asm(new_split_all_lines)
    elif current_op == "jmp":
        new_split_all_lines[i][0] = "nop"
        run_asm(new_split_all_lines)
