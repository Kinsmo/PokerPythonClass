def make_poker():
    numbers = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] 
    suits = ['\u2660', '\033[1;31m\u2665\033[0m', '\u2663', '\033[1;31m\u2666\033[0m'] 

    all_cards = [(number,suit) for number in numbers for suit in suits]
    return all_cards

def print_poker(pokers):
    for card in pokers:
        print(f"{card[0]}{card[1]}",end = ' ')

class Color:
    red = '\033[1;31m'  
    end = '\033[0m'

def is_flush(hand_pokers):
    return all([hand_pokers[0][1] == poker[1] for poker in hand_pokers])
