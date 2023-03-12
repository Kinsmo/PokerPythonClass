numbers = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] 
suits = ['\u2660', '\033[1;31m\u2665\033[0m', '\u2663', '\033[1;31m\u2666\033[0m'] 

all_cards = [(number,suit) for number in numbers for suit in suits]

for card in all_cards:
    print(f"{card[0]}{card[1]}",end = ' ')
