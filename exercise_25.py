import requests

url = 'https://www.s.cn/list/nike'
headers = {'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
                'accept-encoding': 'gzip, deflate, br',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'referer': 'https://www.s.cn/list/nike',
                'user-agent': 'Chrome/67.0.3396.99',
                'x-requested-with': 'XMLHttpRequest'
                }

req = requests.post(url)
print(req.text)