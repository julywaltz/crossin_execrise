import urllib.request

url = 'https://xueqiu.com/P/ZH1335978'
req = urllib.request.urlopen(url)
html = req.read()

