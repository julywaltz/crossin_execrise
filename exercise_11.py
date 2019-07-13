import requests


def weather():
    print('欢迎使用！')
    choice = input('按任意键开始，输入q退出\n')
    if choice != 'q':
        city = input('\n你想要查询天气的城市：\n')
        url = 'http://wthrcdn.etouch.cn/weather_mini?city={}'.format(city)
        req = requests.get(url)
        data = req.json()
        data_result = data.get('data')
        if data_result:
            forecast = data_result.get('forecast')
            print('\n当前温度：{}℃'.format(data_result.get('wendu')))
            print('{}'.format(data_result.get('ganmao')))
            print('\n五日预报:\n')
            for f in forecast:
                print('{}:{}, {}, {}'.format(f.get('date'),
                                             f.get('high'), f.get('low'), f.get('type')))
            weather()
        else:
            print('未能获取该城市天气状况')
            weather()


weather()
