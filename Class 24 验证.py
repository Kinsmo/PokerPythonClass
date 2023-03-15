from poker import *
import random
from kinspy.print_functions import *

pokers = make_poker()

n_flush = 0
n_test = 1000000

for i in range(n_test):
    random.shuffle(pokers)
    hand_pokers = pokers[0:5]

    if is_flush(hand_pokers) ==  True:
        n_flush += 1
        printred("同花出现了！！")
        print_poker(hand_pokers)

print(f"同花概率： {n_flush/n_test}")
# 0.001997
# ？？？？
# 古典概型
# P(flush) = 同花5张/任意5张
#          = C(4,1)*C(13,5)/C(52,5)
#          = 5148/2598960 
#          = 0.00198079