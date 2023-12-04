"""
Advent of Code 2023 - Day 04
Balazs Borsos
"""

from pathlib import Path
from collections import Counter

EXAMPLE_DATA = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

LOCAL_FOLDER = THIS_DIR = Path(__file__).parent

def get_data() -> str:
    with open(LOCAL_FOLDER / 'input.txt') as f:
        data = f.read()
    return data

def parse_cards(data: str) -> dict:
    cards = {}
    lines = data.split('\n')
    for line in lines:
        if line == "":
            continue
        tmp_split = line.split(':')
        card_name = tmp_split[0]
        winning_nums = [int(s) for s in tmp_split[1].split('|')[0].strip().split()]
        card = [int(s) for s in tmp_split[1].split('|')[1].strip().split()]
        cards[card_name] = {'winning_nums': winning_nums, 'card': card}

    return cards

def solve(cards: dict, stage_two: bool = False) -> int:
    
    if stage_two:
        card_cache = [i for i in range(1,len(cards)+1)]
        for card in cards:
            card_num = int(card.split()[1])
            n_matches = len(set(cards[card]['winning_nums'])&set(cards[card]['card']))
            card_list = [i for i in range(card_num+1, card_num + n_matches+1)]
            counts = Counter(card_cache)
            if card_list:
                for _ in range(counts[card_num]):
                    card_cache.extend(card_list)
        score = sum([counts[i] for i in counts])
        
    else:
        points = 0
        for card in cards:
            card_num = int(card.split()[1])
            n_matches = len(set(cards[card]['winning_nums'])&set(cards[card]['card']))
            card_score = 2 ** (n_matches - 1) if n_matches > 0 else 0
            points += card_score
        score = points

    return score

if __name__ == "__main__":
    data = get_data()
    cards = parse_cards(data)
    print(f'The final score is: {solve(cards,True)} points')

