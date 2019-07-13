import pygal
from die import Die
# 创建六面骰子
die_1 = Die(6)
die_2 = Die(16)
# 创建存储结果的列表
results = []

for roll_num in range(1000000000):
    result = die_1.roll_die()+die_2.roll_die()
    results.append(result)

# 创建每个点数出现次数的列表
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "D6和D16骰子投掷1亿次点数和的结果"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22']
hist.x_title = "骰子点数和"
hist.y_title = "出现次数"

hist.add("D6+D16",frequencies)
hist.render_to_file('die_vusual_4.svg')

