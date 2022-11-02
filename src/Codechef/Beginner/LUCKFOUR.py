t = int(input())

for i in range(t):
    four_count = 0
    n = input()
    n_list = list(n)

    for char in n_list:
        if char == '4':
            four_count += 1

    print(four_count)
