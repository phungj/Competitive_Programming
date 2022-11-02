import os


def find_chains(current_adapters, current_chain, max_joltage):
    valid_adapters = \
        [adapter for adapter in current_adapters if adapter - current_chain[len(current_chain) - 1] in (1, 2, 3)]

    if not valid_adapters and current_chain[len(current_chain) - 1] != max_joltage:
        return 0
    elif not valid_adapters and current_chain[len(current_chain) - 1] == max_joltage:
        return 1
    else:
        count = 0

        for adapter in valid_adapters:
            copied_adapters = current_adapters.copy()
            copied_adapters.remove(adapter)

            copied_chain = current_chain.copy()
            copied_chain.append(adapter)

            count += find_chains(copied_adapters, copied_chain, max_joltage)

        return count


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

print(find_chains(adapters, [0], max_joltage))


