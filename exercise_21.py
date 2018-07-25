import requests
from bs4 import BeautifulSoup
from threading import Thread

def pic_download(link):
    file_name = link.split('/')[-1]
    print(file_name, "下载中")
    retries = 0
    while retries < 3:
        try:
            req = requests.get(link, timeout=10)
            pic = open(file_name, 'wb')
            pic.write(req.content)
        except requests.exceptions.RequestException as e:
            retries += 1
            print(e)
            print(file_name, '下载失败')
        else:
            print(file_name, '已保存')
            break


url = 'https://www.lifeofpix.com/'
req = requests.get(url)
html =req.text
soup = BeautifulSoup(html,'lxml')
pic_list = soup.find_all('img',class_="img-low-to-high")
for link in pic_list:
    link = link.get('data-src')
    t = Thread(target=pic_download,args=(link,))
    t.start()
