# @thomasrw
# copyright 2018

# import glob
# import subprocess
import axelrod as axl
import itertools
#requires changes to game.py; zero_determinant.py; memoryone.py
#working changes to individual strategies

print("hello world")

# glob.glob('tournament.*')


# print(subprocess.check_output("ls ", shell=True))





axl.seed(0)  # Set a seed
players = [s() for s in axl.demo_strategies]  # Create players
#players = [axl.Cooperator(), axl.Defector(), axl.Random(0.5), axl.TitForTat(), axl.Grudger()]
myplayers = [x for x in itertools.combinations_with_replacement(axl.demo_strategies, 5)]


print(players)
#print(axl.demo_strategies)
print(myplayers)
print(len(myplayers))

playthis = [y() for y in myplayers[0]]
print(playthis)


'''
tournament = axl.Tournament(players)  # Create a tournament
#tournament.prob_end = 100
print("turns equals")
print(tournament.turns)
results = tournament.play()  # Play the tournament
print(results.ranked_names)

# ['Defector', 'Grudger', 'Tit For Tat', 'Cooperator', 'Random: 0.5']

'''
