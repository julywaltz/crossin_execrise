#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Julywaltz
@Date: 2019-06-15 11:16:08
@LastEditors: Julywaltz
@LastEditTime: 2019-06-15 11:19:41
'''
first = input('第一个字:').lower()
second = input('第二个字:').lower()
alphabet = {
    'a': '01',
    'b': '02',
    'c': '03',
    'd': '04',
    'e': '05',
    'f': '06',
    'g': '07',
    'h': '08',
    'i': '09',
    'j': '10',
    'k': '11',
    'l': '12',
    'm': '13',
    'n': '14',
    'o': '15',
    'p': '16',
    'q': '17',
    'r': '18',
    's': '19',
    't': '20',
    'u': '21',
    'v': '22',
    'w': '23',
    'x': '24',
    'y': '25',
    'z': '26'
}

number = alphabet[str(first[0])]
code = 'Pw' + str(len(second)) + second[0].upper() + 'Cyl' + number + str(
    len(first)) + first[0].upper() + 'Wm'
print(code)
