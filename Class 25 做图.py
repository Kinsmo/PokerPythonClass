from poker import *
import random
from kinspy.print_functions import *
from matplotlib import pyplot as plt

pokers = make_poker()

n_flush = 0
n_test = 1000000
p_current = []

for i in range(n_test):
    random.shuffle(pokers)
    hand_pokers = pokers[0:5]

    if is_flush(hand_pokers) ==  True:
        n_flush += 1
    p_current.append(n_flush/(i+1))

plt.plot(p_current)
plt.savefig("fig")
plt.show()

print(f"同花概率： {n_flush/n_test}")
