# -*- coding: utf-8 -*-
import random
import os

# 用户信息存档
def data_write(user_file_path,time):
    time = str(time)
    with open(user_file_path, 'a', encoding='UTF-8') as f_user:
        f_user.writelines(time+'\n')

#用户存档读取
def data_read(user_file_path):
    with open(user_file_path, 'r', encoding='UTF-8') as f_user:
        round = f_user.read().split()
        for time in round:
            time = int(time)
    return round

# 输入正确性判断，游戏运行
def game_start(user_file_path):
    print('猜猜数字是几？')
    time = 1
    while True:
        num = random.randint(1, 100)
        condition = True
        while condition:
            ans = input("第{}次\n请输入100以内的数字:".format(time))
            try:
                ans = int(ans)
                time += 1
                if num < ans:
                    print(str(ans) + ' 太大了')
                elif num > ans:
                    print(str(ans) + ' 太小了')
                else:
                    print('猜中了！ 答案就是 ' + str(ans))
                    data_write(user_file_path, time-1)
                    break
            except:
                condition =True
        choice = input('请输入"go"再玩一次，否则退出游戏:')
        if choice == "go":
            game_start(user_file_path)
        else:
            break
    round = data_read(user_file_path)
    if round != []:
        best = []
        for x in round:
            best.append(int(x))
        best = min(best)
        total = 0
        for x in round:
            total = total+ int(x)
        average = float('%.2f'%(total/len(round)))
        print('\n你猜中一共用了{}次机会\n你一共进行了{}次游戏\n你平均{}次猜中答案\n你的最好成绩是{}次'.
          format(round[-1], len(round), average, best))
        print("游戏结束")

# 读取用户存档文件，不存在则创建用户存档文件，并开始游戏
username = input('username:')
data_path = os.getcwd()+ '/game_data'
folder = os.path.exists(data_path)
if not folder:
    os.makedirs(data_path)
user_list = os.listdir(data_path)
user_file_path = 'game_data/' + username + '.txt'
username_1 = username+'.txt'
if username_1 in user_list:
    print('欢迎回来 {} ,祝您游戏愉快!'.format(username))
    game_start(user_file_path)
elif username_1 not in user_list:
    print('欢迎加入游戏 {} ,祝您游戏愉快!'.format(username))
    with open(user_file_path, 'a', encoding='UTF-8') as f_user:
        time = 1
        game_start(user_file_path)