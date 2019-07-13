# -*- coding:utf-8 -*-
class Medal():
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def increased(self, rangking):
        if rangking == 1:
            self.gold += 1
            print('\n{}增加一枚金牌,金牌数量增加至{}'.format(self.country, self.gold))
        elif rangking == 2:
            self.silver += 1
            print('\n{}增加一枚银牌,银牌数量增加至{}'.format(self.country, self.silver))
        elif rangking == 3:
            self.bronze += 1
            print('\n{}增加一枚铜牌,铜牌数量增加至{}'.format(self.country, self.bronze))

    @property
    def medal_amount(self):
        return self.gold + self.silver + self.bronze

    def __str__(self):
        return '%s: 金 %d , 银 %d , 铜 %d , 总 %d ' % (self.country, self.gold,
                                                   self.silver, self.bronze,
                                                   self.medal_amount)


china = Medal('China', 26, 18, 19)
usa = Medal('USA', 46, 37, 38)
uk = Medal('UK', 27, 23, 17)

print(china)
print(usa)
print(uk)

china.increased(1)

medal_list = [china, usa, uk]

medal_list = sorted(medal_list, key=lambda x: x.gold, reverse=True)
print('\n按金牌数量排名')
for c in medal_list:
    print(c)

medal_list = sorted(medal_list, key=lambda x: x.medal_amount, reverse=True)
print('\n按奖牌总数排名')
for c in medal_list:
    print(c)
