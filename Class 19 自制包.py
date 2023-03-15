from poker import *

# 主代码
pokers = make_poker()

import random
random.shuffle(pokers)
print(f"{Color.red}洗牌!!!{Color.end}")

print_poker(pokers)