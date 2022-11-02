import os
from itertools import groupby
from queue import SimpleQueue


def fill_queue(deck_list):
    deck_list = [int(c) for c in deck_list]
    deck_queue = SimpleQueue()

    for card in deck_list:
        deck_queue.put(card)

    return deck_queue


file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip("\n")

split_decks = [list(group) for k, group in groupby(all_lines, lambda x: x == "") if not k]

for deck in split_decks:
    deck.pop(0)

deck_one = fill_queue(split_decks[0])
deck_two = fill_queue(split_decks[1])
card_one = 0
card_two = 0

while not deck_one.empty() and not deck_two.empty():
    card_one = deck_one.get()
    card_two = deck_two.get()

    if card_one > card_two:
        deck_one.put(card_one)
        deck_one.put(card_two)
    else:
        deck_two.put(card_two)
        deck_two.put(card_one)

score = 0
winning_deck = deck_one if not deck_one.empty() else deck_two

for i in range(winning_deck.qsize(), 0, -1):
    score += i * winning_deck.get()

print(score)
