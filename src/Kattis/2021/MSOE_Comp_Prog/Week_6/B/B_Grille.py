from itertools import chain


def apply_grille(plaintext, ciphertext):
    for r in range(len(grille)):
        for c in range(len(grille[0])):
            if grille[r][c] == ".":
                plaintext[r][c] = ciphertext[:1]
                ciphertext = ciphertext[1:]

    return plaintext, ciphertext


def rotate_grille(grille):
    return list(zip(*grille[::-1]))


num_lines = int(input())
grille = [[0 for x in range(num_lines)] for y in range(num_lines)]
plaintext = [['' for x in range(num_lines)] for y in range(num_lines)]
current_line = ''

for i in range(num_lines):
    current_line = input()

    for j in range(len(current_line)):
        grille[i][j] = current_line[j]

ciphertext = input()


for i in range(4):
    plaintext, ciphertext = apply_grille(plaintext, ciphertext)
    grille = rotate_grille(grille)

final_plaintext = ''.join(list(chain.from_iterable(plaintext)))

if not len(final_plaintext) == len(grille) ** 2:
    print("invalid grille")
else:
    print(final_plaintext)
