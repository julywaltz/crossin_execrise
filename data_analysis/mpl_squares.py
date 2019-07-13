import matplotlib.pyplot as plt

input_velues = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_velues,squares,linewidth=5)

plt.title("squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=24)
plt.ylabel("Square of Value",fontsize=24)

plt.tick_params(axis='both',labelsize=24)
plt.show()