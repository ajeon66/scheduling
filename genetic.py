import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pandas
import numpy as np
import random
import math

import structure as s

def genetic(people, ind, cycles):
	Pop = s.Duty(people, ind)

	best = []
	for i in range(cycles):
		print("Generation: \n{}".format(Pop.gentable))
		print("Fitness: \n{}".format(Pop.fitness))
		Pop.newpop()
		best.append(Pop.best_fitness())
		print("Cycle: {} \n{}".format(i, Pop.return_optimal()))

	print(Pop.return_optimal())

	#plots best results per cycle
	plt.plot(best, 'b.-')
	plt.xlabel('Generation')
	plt.show()

genetic(['a','b','c','d','e','f'], 100, 10)

