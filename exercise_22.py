import requests
import csv




title_list = []
all_auther = []
shown_offset = 1559916066000001
for i in range(0,10):
    url = 'https://www.csdn.net/api/articles?type' \
          '=more&category=newarticles&shown_offset={}'.format(shown_offset)
    req = requests.get(url)
    data_list = req.json()
    for data in data_list['articles']:
        if data['title'] not in title_list:
            print(data['title'], data['user_name'], data['views'])
            all_auther.append([data['title'], data['user_name'], data['views']])
            title_list.append(data['title'])
    shown_offset = data_list['shown_offset']
    print(shown_offset)
with open('CSDN_article.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['标题','作者','阅读量'])
    for line in all_auther:
        writer.writerow(line)