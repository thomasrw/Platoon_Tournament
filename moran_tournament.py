# @thomasrw
# copyright 2018

import axelrod as axl
import itertools
import pickle
import random
import matplotlib.pyplot as plt

mp_prefix = "/home/thomasrw/Desktop/platoon_tournament_results_mp/"

def instance_file_MP(input,f):
    with open(f, 'wb') as handle:
        pickle.dump(input, handle)

def recover_results(p,r):
    file_path = p
    run_number = r

    with open(file_path + 'mp' + str(run_number), 'rb') as handle:
        recovered_populations = pickle.load(handle)
    return recovered_populations

axl.seed(0)  # Set a seed
players = [s() for s in axl.demo_strategies]  # Create players
players = players + players + players + players + players + players + players + players + players + players



mp = axl.MoranProcess(players, turns=10)

print("let the games begin")
populations = mp.play()
print(mp.winning_strategy_name)
print(len(mp))

instance_file_MP(populations, mp_prefix + 'mp' + '10')
old_population = recover_results(mp_prefix, 10)

ax = mp.populations_plot()
plt.show()

print(populations)
print(old_population)

mp2 = axl.MoranProcess([])
mp2.populations = old_population

ax = mp2.populations_plot()
print(len(mp2))
plt.show()