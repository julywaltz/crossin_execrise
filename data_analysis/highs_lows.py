import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'date/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 创建一个列表存储最高温度
    dates,highs,lows= [],[],[]
    # 遍历文件余下各行，并将每行第二个元素存入列表
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        highs.append(int(row[1]))
        lows.append(int(row[2]))

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='red',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='Blue',alpha=1)
plt.title('Daily high temperetures',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('TmperetuireF',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

