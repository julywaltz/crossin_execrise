import os

file_list = os.listdir(os.getcwd())
with open('file_list.txt', 'r', encoding="UTF-8") as f:
    lines = f.read().splitlines()
    print(lines)
    nums = []
    for num in lines:
        num = int(num)
        print(num)
        nums.append(num)
    print(nums)
    num = max(nums)+1
    print(num)
file_name = 'exercise_'+str(num)+'.py'
open(file_name, 'w')

with open('file_list.txt','a',encoding='UTF-8') as f:
    f.writelines(str(num)+'\n')