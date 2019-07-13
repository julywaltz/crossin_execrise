import requests
import re
import os

data_path = os.getcwd() + '/image'
folder = os.path.exists(data_path)
if not folder:
    os.makedirs(data_path)
start_page = int(input('开始'))
end_page = int(input('结束'))
for page in range(start_page,end_page+1) :
      url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
      req = requests.get(url)
      list = re.findall(r'/pictures/.*?jpeg|/pictures/.*?.jpg|/pictures/.*?png|/pictures/.*?.gif', req.text)
      for pic in list:
            url = 'http://pic.qiushibaike.com/system'+ pic
            req = requests.get(url)
            pic_name = pic.split('/')[-1]
            with open('image/{}'.format(pic_name), 'wb')as f:
                  f.write(req.content)
                  print('{} 下载成功'.format(pic_name))
