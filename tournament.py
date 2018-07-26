# @thomasrw
# copyright 2018

# import glob
# import subprocess
import axelrod as axl
import itertools
import pickle
import marshal
import json
#requires changes to game.py; zero_determinant.py; memoryone.py
#working changes to individual strategies not required
#resolving dependencies required installing some older software versions

print("hello world")

# glob.glob('tournament.*')


# print(subprocess.check_output("ls ", shell=True))





axl.seed(0)  # Set a seed
players = [s() for s in axl.demo_strategies]  # Create players
#players = [axl.Cooperator(), axl.Defector(), axl.Random(0.5), axl.TitForTat(), axl.Grudger()]
#myplayers = [x for x in itertools.combinations_with_replacement(axl.demo_strategies, 10)]
c = itertools.combinations_with_replacement(axl.demo_strategies, 50)
counter = sum( 1 for _ in c)
print(counter)
#316251



myplayers = itertools.combinations_with_replacement(axl.demo_strategies, 50)

print(players)
#print(axl.demo_strategies)
#print(myplayers)


#playthis = [y() for y in myplayers[0]]

file_prefix = "/home/thomasrw/Desktop/"
#f = open(file_prefix + 'run1', 'w')


for z in range(2):
    playthis = [y() for y in next(myplayers)]
    #print(playthis)
    tournament = axl.Tournament(playthis, turns=10)
    results = tournament.play(filename=file_prefix + 'run' + str(z+1))
    print(results.ranked_names)

#TODO reconstitute result_set object from file generated previously by tournament.play()



'''
tournament = axl.Tournament(players)  # Create a tournament
#tournament.prob_end = 100
print("turns equals")
print(tournament.turns)
results = tournament.play()  # Play the tournament
print(results.ranked_names)

# ['Defector', 'Grudger', 'Tit For Tat', 'Cooperator', 'Random: 0.5']

'''
