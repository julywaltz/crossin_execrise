#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-06-26 22:43:17
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-06-26 23:36:44
# @Email: julywaltz77@hotmail.com
import pandas as pd
import json
from urllib.request import urlopen, quote
import csv
import traceback
import os


ak = 'hfdGL6WkrvzTe7hrGVMl1AnEO1C336KK'
add = quote('凯撒花园')  # 本文城市变量为中文，为防止乱码，先用quote进行编码
url = 'http://api.map.baidu.com/geocoding/v3/?address={}&output=json&ak={}&callback=showLocation'.format(add, ak)
req = urlopen(url)
res = req.read().decode().strip('showLocation&&showLocation(').strip(')')
print(res, type(res))
c = str(8300).strip()
temp = json.loads(res)
file = open('经纬度.json', 'w')  # 建立json数据文件
try:
    lng = temp['result']['location']['lng']
    print(lng)
    lat = temp['result']['location']['lat']
    print(lat)
    str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) + '},'
    print(str_temp, type(str_temp))
    file.write(str_temp)
except:
    f = open("异常日志.txt", 'a')
    traceback.print_exc(file=f)
    f.flush()
    f.close()
