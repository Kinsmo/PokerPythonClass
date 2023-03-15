from poker import *
import random
from kinspy.print_functions import *

pokers = make_poker()

# 0.04 %
# 0.02 %
# 0.03 %

for i in range(1000):
    random.shuffle(pokers)
    hand_pokers = pokers[0:5]

    if is_flush(hand_pokers) ==  True:
        printred("同花出现了！！")
        print_poker(hand_pokers)
