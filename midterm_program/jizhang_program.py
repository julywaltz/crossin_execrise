# -*- coding: utf-8 -*-

import time
import os


#记录流水账单
def keep_account():
    print('\n记账模式')
    deals = input("交易对象：")
    income = input("收入/万元：")
    expenses = input("支出/万元：")
    acc_rec = input("应收账款/万元：")
    acc_pay = input("应付账款/万元：")
    t = time.localtime()
    date = time.strftime("%Y-%m-%d", t)
    cash = [deals,income,expenses,acc_rec,acc_pay,date]
    cash = ' '.join(cash)
    cash_0 =['交易对象','收入','支出','应收账款','应付账款','交易时间']
    cash_0 = ' '.join(cash_0)
    file_list = os.listdir(os.getcwd())
    if 'cash_flow_statements.txt' in file_list:
        with open('cash_flow_statements.txt','a',encoding='UTF-8') as f_cash:
            f_cash.writelines(cash+'\n')
    else:
        with open('cash_flow_statements.txt','a',encoding='UTF-8') as f_cash:
            f_cash.writelines(cash_0 + '\n'+cash+'\n')


def cash_read():
    with open('cash_flow_statements.txt','r',encoding="UTF-8") as f_cash:
        cash = []
        lines = f_cash.read().splitlines()
        for x in lines[1:]:
            items = []
            x = x.split()
            for y in x[1:-1]:
                y = int(y)
                items.append(y)
            cash.append(items)
        return cash

#资产负债表文件初始化
def balance_sheet():
    file_list = os.listdir(os.getcwd())
    balance_0 = ['结算日期','资产/万元','负债/万元','净资产/万元']
    balance_0 = ' '.join(balance_0)
    if 'balance_sheet.txt' not in file_list:
        t = time.localtime()
        date = time.strftime("%Y-%m-%d", t)
        balance_1 = [date, '0', '0', '0']
        balance_1 = ' '.join(balance_1)
        with open('balance_sheet.txt', 'a', encoding='UTF-8') as f_balance:
            f_balance.writelines(balance_0+'\n'+balance_1+'\n')


# 资产负载表读取
def balance_read():
    with open('balance_sheet.txt', 'r', encoding='UTF-8') as f_balance:
        balance = []
        lines = f_balance.read().splitlines()
        for line in lines[1:]:
            line = line.split()
            items = []
            for x in line[1:]:
                x = int(x)
                items.append(x)
        balance.append(items)
        return balance

#资产负债表写入
def balance_write(new_assets,new_debt,new_net_assets):
    t = time.localtime()
    date = time.strftime("%Y-%m-%d", t)
    new_balance = [date, str(new_assets),str(new_debt),str(new_net_assets)]
    new_balance = ' '.join(new_balance)
    with open('balance_sheet.txt', 'a', encoding='UTF-8') as f_balance:
        f_balance.writelines(new_balance + '\n')


# 查询最近十笔交易
def query_a():
    with open('cash_flow_statements.txt', 'r', encoding="UTF-8") as f_cash:
        lines = f_cash.read().splitlines()
        title = lines[0].split()
        if len(lines) >= 11:
            print('{}  {}  {}  {}  {}  {}'.format(title[0],title[1],title[2],title[3],title[4],title[5]))
            for i in range(1,10):
                x = []
                for y in lines[-i].split():
                    x.append(y)
                print('{}   {}万  {}万  {}万   {}万   {}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))

        else:
            print('{}  {}  {}  {}  {}  {}'.format(title[0], title[1], title[2], title[3], title[4], title[5]))
            for i in range(1,len(lines)):
                x = []
                for y in lines[-i].split():
                    x.append(y)
                print('{}   {}万  {}万  {}万   {}万   {}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))

#查询单一对象交易流水
def query_b():
    query_object = input('请输入公司名：')
    with open('cash_flow_statements.txt', 'r', encoding="UTF-8") as f_cash:
        lines = f_cash.read().splitlines()
        num = []
        for line in lines:
            if query_object in line:
                report = line.split()
                num.append(line)
                print('\n与{}公司共有{}笔交易'.format(query_object, len(num)))
                print('交易时间：{}\n收入：{}\n支出：{}\n应收账款：{}\n应付账款：{}\n'.format(report[-1], report[1],
                                                                          report[2], report[3], report[4]))




# 主程序
def main_program():
    print('1.查账；2.记账')
    choice = input('请选择服务：')
    if choice == '1':
        file_list = os.listdir(os.getcwd())
        with open('cash_flow_statements.txt', 'r', encoding="UTF-8") as f_cash:
            lines = f_cash.read().splitlines()
        if 'cash_flow_statements.txt' in file_list and len(lines)> 1:
            print('\n查询模式 \n1.查询最近十笔交易记录 \n2.查询与某公司交易往来 \n3.查询最近资产负债状况' )
            choice_1 = input('请选择服务：')
            if choice_1 == '1':
                query_a()
                main_program()
            elif choice_1 == '2':
                query_b()
                main_program()
            elif choice_1 == '3':
                with open('balance_sheet.txt', 'r', encoding='UTF-8') as f_balance:
                    lines = f_balance.read().splitlines()
                    report = lines[-1].split()
                    print('\n最新资产：{}\n最新负债：{}\n最新净资产：{}\n最后更新时间：{}'.format(report[1],report[2],
                            report[3],report[0]))
                main_program()
        else:
            print('无记录')
            main_program()

    elif choice == '2':
        keep_account()
        cash = cash_read()
        balance_sheet()
        balance = balance_read()
        new_assets = balance[-1][0] + cash[-1][0] - cash[-1][1]
        new_debt = balance[-1][1] + cash[-1][3] - cash[-1][2]
        new_net_assets = new_assets - new_debt

        print('\n交易已记录\n当前资产状况')
        print('最新资产：{}万 \n最新负债：{}万 \n最新净资产：{}万'.format(new_assets, new_debt, new_net_assets))
        balance_write(new_assets,new_debt,new_net_assets)
        main_program()


main_program()
