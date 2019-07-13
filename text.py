# coding = utf-8

from bs4 import BeautifulSoup
import requests
from lxml import etree
import threading


url = 'https://www.s.cn/umbro-UO182AP2502-401.html'
req = requests.get(url)
tree = etree.HTML(req.text)
goods_info = tree.xpath('//ul[@class = "goodsprops clearfix"]/*')
for info in goods_info:
  print(info.xpath('//text()'))
