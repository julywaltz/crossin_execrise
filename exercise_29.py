import random

times = []
while True:
    ans = random.randint(1, 100)
    time = 0
    while True:
        if time < 10:
            time += 1
            num = int(input('猜猜数字是几：'))
            if num > ans:
                print('这是你第%d次猜，你猜大了' % time)
            elif num < ans:
                print('这是你第%d次猜，你猜小了' % time)
            else:
                print('这是你第%d次猜，你猜对了' % time)
                times.append(time)
                break
        else:
            print('你猜的次数超过10次，你输了')
            times.append(10)
            break
    print(times)
    choice = input('你还要继续吗？继续请按任意键，退出继续请输入N')
    if choice == 'N':
        if times != [10]:
            print('你一共玩了%d轮，平均%d次猜对' % (len(times), sum(times) / len(times)))
        break
