import os
from itertools import groupby
from queue import Queue


def fill_queue(deck_list):
    deck_list = [int(c) for c in deck_list]
    deck_queue = Queue()

    for card in deck_list:
        deck_queue.put(card)

    return deck_queue

# TODO: Figure this out
def recursive_combat(deck_one, deck_two, deck_one_list, deck_two_list, player_one_cards, player_two_cards):
    if list(deck_one.queue) in deck_one_list and list(deck_two.queue) in deck_two_list:
        return True, player_one_cards, player_two_cards
    else:
        deck_one_list.append(deck_one)
        deck_two_list.append(deck_two)

        card_one = deck_one.get()
        card_two = deck_two.get()

        player_one_cards.append(card_one)
        player_two_cards.append(card_two)

        if card_one > len(list(deck_one.queue)) and card_two > len(list(deck_two.queue)):
            recursive_combat(deck_one, deck_two, deck_one_list, deck_two_list, player_one_cards, player_two_cards)
        else:
            if card_one > card_two:
                return True, player_one_cards, player_two_cards
            else:
                pass


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


