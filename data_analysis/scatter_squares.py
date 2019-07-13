import matplotlib.pyplot as plt

x_values = list(range(1,10001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c='red',edgecolors='none',s=40)

plt.title("Squares Numbers",fontsize = 24)
plt.xlabel("Values",fontsize = 24)
plt.ylabel("Square of values",fontsize = 24)

plt.tick_params(axis='both',which='minor',labelsize=24)
plt.axis([0,11000,0,100000000])
plt.savefig('squares_plot.png',bbox_inches='tight')