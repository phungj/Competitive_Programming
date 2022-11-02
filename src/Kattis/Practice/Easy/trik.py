current_cup = 1

for move in list(input()):
    if move == "A":
        if current_cup == 1:
            current_cup = 2
        elif current_cup == 2:
            current_cup = 1
    elif move == "B":
        if current_cup == 2:
            current_cup = 3
        elif current_cup == 3:
            current_cup = 2

    else:
        if current_cup == 1:
            current_cup = 3
        elif current_cup == 3:
            current_cup = 1

print(current_cup)
