from poker import *
import random
from kinspy.print_functions import *
from matplotlib import pyplot as plt
import tqdm

pokers = make_poker()

n_flush = 0
n_test = 1000000
p_current = []
progress_bar = tqdm.tqdm(total = 100)

for i in range(n_test):
    progress_bar.update(100/n_test)
    random.shuffle(pokers)
    hand_pokers = pokers[0:5]

    if is_flush(hand_pokers) ==  True:
        n_flush += 1
    p_current.append(n_flush/(i+1))

p = 5148/2598960
plt.axhline(p)
plt.plot(p_current)
plt.savefig("fig")
plt.show()

print(f"同花概率： {n_flush/n_test}")