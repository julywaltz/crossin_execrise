# 原练习代码：
# import string
#import random

#concession_code  = []
#for x in range(0,200):
#    list = string.ascii_letters
#    code_list = []
#    for y in range(0,8):
#        code_list.append(list[random.randint(0,51)])
#        code = "".join(code_list)
#    concession_code.append(code)
#print(concession_code)

#学习本课后的修改为：

import string
import random

#利用choice方法：
#concession_code = []
#while len(concession_code)<200:
#    list = string.ascii_letters
#    code_list_1 = []
#    for i in range(0,8):
#        code_list.append(random.choice(list))
#        code = "".join(code_list)
#    if code not in concession_code: #新增加避免重复优惠码出现条件
#        concession_code.append(code)
#print(concession_code)

#利用sample方法：
#concession_code = []
#while len(concession_code)<200:
#    list = string.ascii_letters
#    code = "".join(random.sample(list,8))
#    if code not in concession_code:
#        concession_code.append(code)
#print(concession_code)

#利用shuffle方法：
concession_code = []
while len(concession_code) < 200:
    code_list = list(string.ascii_letters)
    random.shuffle(code_list)
    code = "".join(code_list[:8])
    if code not in concession_code:
        concession_code.append(code)

print(concession_code)
