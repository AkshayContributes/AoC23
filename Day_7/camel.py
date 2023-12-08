from pathlib import Path


def parse_input():
    data = []
    lines = Path('input.txt').read_text().split('\n')
    for line in lines:
        hand, bid = line.split(' ')
        data.append((hand, int(bid)))
    return data


letter_map = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}

letter_map_2 = {'T': 'A', 'J': '.', 'Q': 'C', 'K': 'D', 'A': 'E'}


def all_replacements(hand):
    if hand == "":
        return [""]

    return [
        x + y
        for x in ('23456789TQKA' if hand[0] == 'J' else hand[0])
        for y in all_replacements(hand[1:])
    ]


def type_with_joker(hand):
    return max(map(type_of_hand, all_replacements(hand)))


def type_of_hand(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 7
    if 4 in counts:
        return 6
    if 3 in counts:
        if 2 in counts:
            return 5
        return 4
    if counts.count(2) == 4:
        return 3
    if 2 in counts:
        return 2
    return 1


def strength(hand):
    return (type_of_hand(hand), [letter_map.get(card, card) for card in hand])


def strength_joker(hand):
    return (type_with_joker(hand), [letter_map_2.get(card, card) for card in hand])


hands = parse_input()

hands.sort(key=lambda hand: strength(hand[0]))

total = 0

for rank, (hand, bid) in enumerate(hands, 1):
    total += bid * rank

total2 = 0

hands.sort(key=lambda hand: strength_joker(hand[0]))

for rank, (hand, bid) in enumerate(hands, 1):
    total2 += bid * rank

print(total)

print(total2)
