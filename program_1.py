# -*- coding: utf-8 -*-
# 获取列表倒数第二个元素
def takeTotal(elem):
    return elem[-2]

# 读取成绩文件
with open('report.txt',encoding='UTF-8') as f:
    lines = f.read().splitlines()

# 计算总分平均分并排序
name_score = []
i = 1
for line in lines[1:]:
    line = line.split()
    scores = line[1:]
    total = 0
    for score in scores:
        total += int(score)
    average = float(total)/float(len(line)-1)
    average = float('%.2f'%average)
    line.append(total)
    line.append(average)
    name_score.append(line)
name_score.sort(reverse=True,key=takeTotal)
i = 1
for line in name_score:
    line.insert(0,i)
    i += 1

# 计算各科平均分及总平均分
line_0 = [0,'平均',0,0,0,0,0,0,0,0,0,0,0]
for line in name_score:
    for i in range(2,13):
        line_0[i] = float('%.2f'%(float(line_0[i])+float(line[i])/len(name_score)))
name_score.insert(0,line_0)


# 低于60分替换为不及格
n = []
for line in name_score:
    l = line[:2]
    for s in line[2:]:
        if int(s) < 60:
            s = "不及格"
        l.append(s)
    n.append(l)
name_score = n

#输出文件
report = []
title = ['名次','姓名','语文','数学','英语','物理','化学','生物','政治','历史','地理','总分','平均分']
name_score.insert(0,title)
for line in name_score:
    for i in range(0,13):
        line[i] = str(line[i])
    line =  ' '.join(line)
    report.append(line)
report = '\n'.join(report)
print(report)
with open('report_result.txt','w',encoding='UTF-8',) as f_result:
    f_result.write(report)









