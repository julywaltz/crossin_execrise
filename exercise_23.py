import requests
import pymongo
import time

client =pymongo.MongoClient()
db = client.wangyiyun
collections = db.playlists
col_lyric = db.lyric

def get_info(id,headers):
    url = 'http://music.163.com/api/playlist/detail?id={}&updateTime=-1'.format(id)
    req = requests.get(url, headers=headers)
    data = req.json()
    collections.update_one({'id':id}, {'$set': data['result']}, upsert=True)


def get_lyric(id):
    try:
        url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'.format(id)
        headers = {
            'cookie': 'appver=1.5.0.74771',
            'Referer': 'http://music.163.com',
            'User-Agent': 'Chrome/67.0.3396.99'
        }
        req = requests.get(url, headers=headers)
        data = req.json()
        print('下载中')
        col_lyric.update_one({'id': music['id']}, {'$set': data}, upsert=True)
        print('完成')
    except Exception as e:
        print(e)

url = 'http://music.163.com/api/search/pc'
headers = {
    'cookie': 'appver=1.5.0.74771',
    'Referer': 'http://music.163.com'
}
data = {'s': '程序员', 'offset': 0, 'limit': '10', 'type': '1000'}
req = requests.post(url=url, headers=headers, data=data)
data = req.json()
playlists = data['result']['playlists']
for playlist in playlists:
    id = playlist['id']
    get_info(id)
    time.sleep(0.2)

for playlist in collections.find():
    for music in playlist['tracks']:
         print(music['name'],music['id'],'连接中')
         id =music['id']
         get_lyric(id)
         time.sleep(0.2)

print('下载完成')
