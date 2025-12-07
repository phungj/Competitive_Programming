from functools import reduce

with open('input.txt', 'r') as input_file:
    lines = [reversed(line.strip('\n')) for line in input_file.readlines()]
    operators = ''.join(lines[-1]).split()

    current_operator_index = 0
    current_operands = []

    total = 0

    for digit1, digit2, digit3, digit4 in zip(*lines[:-1]):
        if digit1 == ' ' and digit2 == ' ' and digit3 == ' ' and digit4 == ' ':     
            print(current_operands, operators[current_operator_index], reduce((lambda x, y: x * y) if operators[current_operator_index] == '*' else lambda x, y: x + y, current_operands))

            total += reduce((lambda x, y: x * y) if operators[current_operator_index] == '*' else lambda x, y: x + y, current_operands)

            current_operands = []
            current_operator_index += 1
        else:
            current_operands.append(int(digit1 + digit2 + digit3 + digit4))

    total += reduce((lambda x, y: x * y) if operators[current_operator_index] == '*' else lambda x, y: x + y, current_operands)

    print(total)