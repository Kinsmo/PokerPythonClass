from poker import *
import random

# 主代码
pokers = make_poker()
random.shuffle(pokers)
print(f"{Color.red}洗牌!!!{Color.end}")

hand_pokers = pokers[0:5]

print(f"{Color.red}抽牌!!!{Color.end}")

print_poker(hand_pokers)
