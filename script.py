# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
filename = "medium_maze.txtrecord.dat"
lines = [line.rstrip('\n').split() for line in open(filename)]

fitness_max = [k[-2] for k in lines]
indiv = [k[-1] for k in lines]


plt.plot(np.arange(len(indiv), step=1000), fitness_max[0:len(indiv):1000])
#plt.yticks(np.arange(220, 300, step=10))
#plt.axis([0,70000,0,300])
plt.show()

