import re

file_name = input('输入需要文件名：')
with open(file_name,'r',encoding='utf8') as f:
    words = f.read()
words_list = re.findall(r'\b[A-z]+',words)
num = len(words_list)
print('There are {} words in {}'.format(num,file_name))