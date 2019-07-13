import requests
import re


def main_program():
    search = input('输入：')
    download_list = []
    for page in range(1, 30):
        url = 'https://m.zhongziso.com/list_ctime/{}/{}'.format(search, page)
        req = requests.get(url)
        z_list = re.findall(r'thunder://\w+==', req.text)
        s_list = re.findall(r'size.*?d>', req.text)
        s = []
        for x in s_list:
            x = x[6:-8]
            s.append(x)
        s_list = s
        y = []
        for i in range(0, len(s_list)):
            x = z_list[i] + '/' + s_list[i]
            y.append(x)
        download_l = []
        for i in y:
            x = re.findall(r'==/\w+', i)
            x = x[0][3:]
            y = re.search(r'thunder://\w+==', i)[0]
            if float(x) > 900 or float(x) < 2:
                if y not in download_l:
                    download_l.append(y)
        download_l = '\n'.join(download_l)
        download_list.append(download_l)
    download_list = '\n'.join(download_list)
    with open('download_list{}.txt'.format(search), 'a', encoding='utf8') as f:
        f.writelines(download_list + '\n')
    print('下载完毕')


main_program()