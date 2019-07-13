import matplotlib.pyplot as plt
from random_walk import Random_walk

while True:
    rw = Random_walk(1000000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
                edgecolors='none',s=1)
    plt.scatter(0, 0, c='black', s=10)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='black', s=10)

    plt.show()
    keep_running = input('make another walk? Y/N ')
    if keep_running == 'N':
        break
