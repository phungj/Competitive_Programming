from sys import stdin

for line in stdin:
    split_input = line.split(" ")
    print(abs(int(split_input[0]) - int(split_input[1])))
