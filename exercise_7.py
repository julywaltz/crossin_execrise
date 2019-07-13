import random

#生成扑克牌
suit = ('Spade','Heart','Diamond','Club')
points = ('A',2,3,4,5,6,7,8,9,10,'J','Q','K')
cards = []
for x in suit:
    for y in points:
        card = (x,y)
        cards.append(card)
cards.append('red joker')
cards.append('black joker')
#洗牌
random.shuffle(cards)
#发牌
player_a = []
player_b = []
player_c = []
for i in range(0,51):
    if i%3 == 0:
        player_a.append(cards[i])
    elif i%3 == 1:
        player_b.append(cards[i])
    else:
        player_c.append(cards[i])
remain_cards = cards[-3:]

print(player_a)
print(player_b)
print(player_c)
print(remain_cards)
