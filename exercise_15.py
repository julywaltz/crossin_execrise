import requests
import re
import os
import _thread

req_headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
req = requests.get('https://www.qiushibaike.com/imagrank/page/1/',
                   headers=req_headers)
list = re.findall(
    r'/pictures/.*?jpeg|/pictures/.*?.jpg|/pictures/.*?png|/pictures/.*?.gif',
    req.text)
req_fn = 'req_1.txt'
req_f = open(req_fn, 'w', encoding='utf8')
req_f.write(req.text)
req_f.close()
list = re.findall(
    r'/pictures/.*?jpeg|/pictures/.*?.jpg|/pictures/.*?png|/pictures/.*?.gif',
    req.text)
list = '\n'.join(list)
list_f = open('list_1.txt', 'w', encoding='utf8')
list_f.writelines(list)
list_f.close()