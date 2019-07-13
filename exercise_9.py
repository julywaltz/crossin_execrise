import os
file_path = input('指定文件夹名字：')
file_list = os.listdir(file_path)

key_word_file = []
key_word = input('输入检索的关键字：')
for line in file_list:
    if key_word in line:
        key_word_file.append(line)

for line in file_list:
    with open(file_path+'/'+line) as f:
        if key_word in f.read().splitlines() and line not in key_word_file:
            key_word_file.append(line)
print(key_word_file)

