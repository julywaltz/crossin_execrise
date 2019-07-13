import requests
from lxml import etree


# 获取好笑数和评论数
def vot_comment(div):
    vote = div.xpath('../div/span[@class = "stats-vote"]/i/text()')[0]
    comments = div.xpath('../div/span[@class = "stats-comments"]/a/i/text()')[0]
    vots_comments = '\n好笑数：'+ vote + '\n评论数：'+ comments+ '\n'
    return vots_comments



# 获取段子的全文
def contents(div):
    c_div = div.xpath('../a/div/span[@class = "contentForAll"]/text()')
    if c_div != []:
        a_href = div.xpath('../a/@href')[0]
        url = 'https://www.qiushibaike.com/%s'%a_href
        req = requests.get(url)
        html = req.text
        tree = etree.HTML(html)
        content = tree.xpath('//dic[@class = "content"]/text()')[0]
        c_txt = c_txt = '\n' + content[0].strip('\n')
        return c_txt
    else:
        content = div.xpath('../a/div/span/text()')
        c_txt = '\n' + content[0].strip('\n')
        return c_txt

url = 'http://jandan.net/ooxx/page-%s/' % page
req = requests.get(url)
html = req.text
tree = etree.HTML(html)
first = tree.xpath('//div[@class="author clearfix"]')
for div in first:
    auther = div.xpath('./a/h2/text()')
            if auther == []:
                dz.append('\n匿名用户\n性别不详，年龄不详')
                c_txt = contents(div)
                dz.append(c_txt)
                v_c = vot_comment(div)
                dz.append(v_c)
            else:
                gender = div.xpath('./div[@class = "articleGender manIcon"]')
                if gender != []:
                    age = div.xpath('./div[@class = "articleGender manIcon"]/text()')[0]
                    a = '\n作者：' + auther[0].strip('\n') + '\n性别：男，年龄：' + age
                    dz.append(a)
                else:
                    age = div.xpath('./div[@class = "articleGender womenIcon"]/text()')[0]
                    a = '\n作者：' + auther[0].strip('\n ') + '\n性别：女，年龄：' + age
                    dz.append(a)
                c_txt = contents(div)
                dz.append(c_txt)
                v_c = vot_comment(div)
                dz.append(v_c)

main_program()