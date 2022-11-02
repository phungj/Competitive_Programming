import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    current_num = int(all_lines[i])

    for num in all_lines[i+1:]:
        num = int(num)
        sum = current_num + num

        if sum == 2020:
            product = current_num * num
            print(product)