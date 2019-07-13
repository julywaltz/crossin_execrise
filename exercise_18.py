import urllib.request
import re

url = 'http://jandan.net/duan'
req = urllib.request.Request(url)
req.add_header('User-Agent','Chrome / 67.0.3396.99')
response = urllib.request.urlopen(req,timeout=3)
html = response.read()
html_str = html.decode('utf8')

pattern = re.compile('</a></span><p>([\s\S]*?)</p>\n</div>\n<div class="jandan-vote">')


groups = pattern.findall(html_str)
for text in groups:
    text = text.replace('<br />','')
    text = text.replace('</p>', '')
    text = text.replace('<p>', '')
    print(text)
    print('------------')