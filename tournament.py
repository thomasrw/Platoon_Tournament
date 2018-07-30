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
print(myplayers)


#playthis = [y() for y in myplayers[0]]

file_prefix = "/home/thomasrw/Desktop/platoon_tournament_results/"
#fk = open(file_prefix + 'run-players', 'w')

pickle_file = file_prefix + 'players'

playthis = []
#playthis[0] = []
counter = 0

def instance_file(input,f):
    with open(f, 'wb') as handle:
        pickle.dump(input, handle)
    #return input()

#316251

#skip function - put in number of last completed run
spacer = 0
for z in range(400):
    next(myplayers)
    spacer += 1

#put in number of runs to work
for z in range(3600):
    playthis = [y() for y in next(myplayers)]
    instance_file(playthis, pickle_file + '-run' + str(z+spacer+1))
    tournament = axl.Tournament(playthis, turns=10)
    results = tournament.play(filename=file_prefix + 'run' + str(z+spacer+1))
    print(results.ranked_names)


#TODO reconstitute result_set object from file generated previously by tournament.play()

print("break break")

#fk.close()

with open(pickle_file + '-run1', 'rb') as handle:
    played = pickle.load(handle)

print(played)

#played2 = [p() for p in played]

myfile = file_prefix + 'run1'
print(counter)
secondresults = axl.ResultSet(myfile, players=played, repetitions=10)
print(secondresults.ranked_names)



'''
tournament = axl.Tournament(players)  # Create a tournament
#tournament.prob_end = 100
print("turns equals")
print(tournament.turns)
results = tournament.play()  # Play the tournament
print(results.ranked_names)

# ['Defector', 'Grudger', 'Tit For Tat', 'Cooperator', 'Random: 0.5']

'''
