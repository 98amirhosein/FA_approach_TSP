#!/usr/bin/python3
import time

from fireflies import *
import random
import matplotlib.pyplot as plt
from City import *

#
# def draw(points):
#     points = list(points)
#     points = points + points[:1]
#     cities = map(lambda i: (i.x, i.y), points)
#     (x, y) = zip(*cities)
#     plt.scatter(x, y)
#     plt.plot(x, y)
#     plt.show()


if __name__ == '__main__':
    locations = [City(58, 16), City(62, 40), City(3, 20), City(60, 33), City(94, 91),
                 City(30, 68), City(16, 84), City(1, 39), City(40, 30), City(51, 9),
                 City(27, 88), City(97, 50)]
    # draw(locations)

    for i in range(0,1000):
        print(i)
        start_millis = int(round(time.time() * 1000))
        solver = TSPSolver(locations)
        new_order = solver.run()
        time.time()
        final_millis = int(round(time.time()) * 1000)
        t = final_millis - start_millis
        if t < 0:
            t *= -1
        fi = open("times.csv", 'a')
        fi.write(str(t))
        fi.write('\n')
        fi.close()



        # new_locations = [locations[i] for i in new_order]
        # draw(new_locations)
        print('------------------------------')


