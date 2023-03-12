
numbers = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']  # 13
suits = ["Spade", "Heart", "Club", "Diamond"]  # 4

#(xx,xxx)  元组
# [ xxx]  列表
# for  循环

# 列表解析
all_cards = [(number,suit) for number in numbers for suit in suits]
#              在数字里挑一个
#                                     在花色里挑一个

print(all_cards)