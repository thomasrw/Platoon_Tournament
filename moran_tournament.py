# @thomasrw
# copyright 2018

import axelrod as axl
import itertools
import pickle
import random
import matplotlib.pyplot as plt

axl.seed(0)  # Set a seed
players = [s() for s in axl.demo_strategies]  # Create players
players = players + players + players + players + players + players + players + players + players + players



mp = axl.MoranProcess(players, turns=10)

print("let the games begin")
populations = mp.play()
print(mp.winning_strategy_name)
print(len(mp))

ax = mp.populations_plot()
plt.show()