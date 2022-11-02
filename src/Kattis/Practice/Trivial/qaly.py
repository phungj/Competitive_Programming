qaly = 0

for i in range(int(input())):
    split_current_line = input().split(" ")
    qaly += float(split_current_line[0]) * float(split_current_line[1])

print(qaly)
