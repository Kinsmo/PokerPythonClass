from poker import *
import random
from kinspy.print_functions import *

pokers = make_poker()

# 第一张牌花色 == 每个牌花色
for i in range(100):
    random.shuffle(pokers)
    hand_pokers = pokers[0:5]

    tonghua = all([hand_pokers[0][1] == poker[1] for poker in hand_pokers])
    if tonghua ==  True:
        printred("同花出现了！！")
        print_poker(hand_pokers)
