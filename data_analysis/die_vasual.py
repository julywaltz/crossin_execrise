import pygal
from die import Die
# 创建六面骰子
die = Die(6)
# 创建存储结果的列表
results = []

for roll_num in range(100):
    result = die.roll_die()
    results.append(result)

# 创建每个点数出现次数的列表
frequencies = []

for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "六面骰子投掷100次的结果"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "骰子点数"
hist.y_title = "出现次数"

hist.add("六面骰子",frequencies)
hist.render_to_file('die_vusual.svg')

