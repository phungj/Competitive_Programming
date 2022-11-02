from random import randint, choice, choices
from string import ascii_letters

# s = randint(1, 600)
# r = randint(1, 200)
# f = randint(1, 200)

s = randint(1, 75)
r = randint(1, 25)
f = randint(1, 25)

while r + f > s:
    # s = randint(1, 600)
    # r = randint(1, 200)
    # f = randint(1, 200)

    s = randint(1, 75)
    r = randint(1, 25)
    f = randint(1, 25)

# t = randint(1, 1000)
t = randint(1, 125)

with open("test.txt", 'w') as out:
    out.write(str(s) + " " + str(r) + " " + str(f) + " " + str(t) + "\n")

    r_set = set([])
    f_set = set([])
    s_set = set([])
    all_list = [r_set, f_set, s_set]
    t_set = set([])

    while len(r_set) < r:
        # r_set.add(''.join(choices(ascii_letters, k=16)))
        r_set.add(''.join(choices(ascii_letters, k=4)))

    out.write(' '.join(r_set) + "\n")

    while len(f_set) < f:
        # current_f = ''.join(choices(ascii_letters, k=16))
        current_f = ''.join(choices(ascii_letters, k=4))

        if current_f not in r_set:
            f_set.add(current_f)

    out.write(' '.join(f_set) + "\n")

    while len(s_set) < s - (r + f):
        # current_s = ''.join(choices(ascii_letters, k=16))
        current_s = ''.join(choices(ascii_letters, k=4))

        if current_s not in r_set and current_s not in f_set:
            s_set.add(current_s)

    for i in range(t):
        connections = randint(1, s)

        t_string = str(connections) + " "

        for j in range(connections):
            t_string += ' '.join(choice(all_list))

        t_set.add(t_string + "\n")

    out.writelines(t_set)
