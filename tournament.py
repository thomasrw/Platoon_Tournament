# @thomasrw
# copyright 2018

# import glob
# import subprocess
import axelrod as axl

print("hello world")

# glob.glob('tournament.*')


# print(subprocess.check_output("ls ", shell=True))





axl.seed(0)  # Set a seed
# players = [s() for s in axl.demo_strategies]  # Create players
players = [axl.Cooperator(), axl.Defector(), axl.Random(0.5), axl.TitForTat(), axl.Grudger()]
tournament = axl.Tournament(players, turns=1)  # Create a tournament
#tournament.prob_end = 100
print("turns equals")
print(tournament.turns)
results = tournament.play()  # Play the tournament
print(results.ranked_names)

# ['Defector', 'Grudger', 'Tit For Tat', 'Cooperator', 'Random: 0.5']
