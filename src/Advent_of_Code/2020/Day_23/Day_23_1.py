# cups = list("963275481")
cups = list("389125467")
cups = [int(cup) for cup in cups]
current_cup_index = 0
current_cup = cups[current_cup_index]

for i in range(100):
    selected_cups = [cups[(current_cup_index + 1) % len(cups)],
                     cups[(current_cup_index + 2) % len(cups)],
                     cups[(current_cup_index + 3) % len(cups)]]

    destination_cup = current_cup - 1

    while destination_cup in selected_cups or destination_cup < 1:
        destination_cup -= 1

        if destination_cup < 1:
            destination_cup = 9

    cups.remove(selected_cups[0])
    cups.remove(selected_cups[1])
    cups.remove(selected_cups[2])

    cups.insert(cups.index(destination_cup) + 1, selected_cups[0])
    cups.insert(cups.index(destination_cup) + 2, selected_cups[1])
    cups.insert(cups.index(destination_cup) + 3, selected_cups[2])

    current_cup_index = (current_cup_index + 1) % len(cups)
    current_cup = cups[current_cup_index]

one_cup_index = cups.index(1)

for i in range(one_cup_index + 1):
    cups.append(cups.pop(0))

cups = [str(cup) for cup in cups]

print(''.join(cups[:len(cups) - 1]))


