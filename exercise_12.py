import urllib.request
import json

url = 'https://api.douban.com/v2/movie/top250'
req = urllib.request.urlopen(url)
data = req.read()
print(data)

data_dict = json.loads(data)
print(data_dict.keys())
print(data_dict['title'])