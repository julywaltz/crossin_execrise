# coding = utf-8

from bs4 import BeautifulSoup
import requests
from lxml import etree
import threading
from time import sleep


def down_pic(url, filename):
    pic = requests.get(url)
    print(filename, '下载中')
    with open('pics\\' + filename, 'wb') as f:
        f.write(pic.content)
    print(filename, '下载完成')


page_number = 1
while page_number < 9782:
    url = 'https://pixabay.com/images/search/?pagi=' + str(page_number)
    print('打开' + url)
    page_number += 1
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    result = soup.find_all('div', class_='item')
    for link in result:
        link = 'https://pixabay.com' + link.find('a').get('href')
        print("打开" + link)
        html = requests.get(link).text
        url = etree.HTML(html).xpath('//img[@itemprop="contentURL"]/@srcset')[0].split('1x')[0].strip(' ')
        filename = url.split('/')[-1]
        t = threading.Thread(target=down_pic, args=(url, filename))
        t.start()
        sleep(1)
