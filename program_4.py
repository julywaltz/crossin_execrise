import requests
import re
import os
import threading




def list_make(page):
    url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
    req = requests.get(url)
    list = re.findall(r'/pictures/.*?g', req.text)
    return list


def pic_download(list):
    for pic in list:
        url = 'http://pic.qiushibaike.com/system' + pic
        req = requests.get(url)
        pic_name = pic.split('/')[-1]
        pic_path = 'image/{}'.format(pic_name)
        folder = os.path.exists(pic_path)
        if not folder:
            with open('image/{}'.format(pic_name), 'wb')as f:
                f.write(req.content)
                print('{} 下载成功'.format(pic_name))
        else :
            print('{} 已存在'.format(pic_name))



def pic_get():
    while True:
        start_page = int(input('请输入起始页码：'))
        end_page = int(input('请输入结束页码：'))
        for page in range(start_page, end_page + 1):
            pic_list = list_make(page)
            thread_list = []
            downloading = threading.Thread(target=pic_download, args=(pic_list,))
            thread_list.append(downloading)
            downloading.start()
            for x in thread_list:
                x.join()
        print('下载结束')

        break
    main_program()



def main_program():
    choice = input('欢迎使用，按任意键开始，退出请输入"q":')
    if choice != 'q':
        data_path = os.getcwd() + '/image'
        folder = os.path.exists(data_path)
        if not folder:
            os.makedirs(data_path)
        pic_get()
    else:
        print('欢迎下次使用')


main_program()