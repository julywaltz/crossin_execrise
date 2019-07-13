req_1 = requests.get(url)
    html_1 = req_1.text
    root = etree.HTML(html_1)
    first = root.xpath('//div[@class="col1"]/div/a/@href')
    for url in first:
        url = 'https://www.qiushibaike.com' + url
        if urls != []:
            if url != urls[-1]:
                urls.append(url)
        else:
            urls.append(url)
print('地址获取完成')
text = []
for url in urls:
    req = requests.get(url)
    html = req.text
    root = etree.HTML(html)
    word = root.xpath('//div[@class="word"]/div/text()')
    word = '\n'.join(word)
    auther = '\n作者:' + root.xpath('//span[@class="side-user-name"]/text()')[0]
    number = '\n好笑数：' + root.xpath('//i[@class = "number"]/text()')[0]+'\n'+'\n'
    text.append(word)
    text.append(auther)
    text.append(number)
for line in text:
    with open('qiushibaike.txt','a',encoding='utf8') as f:
        f.write(line)
print('段子写入完成')