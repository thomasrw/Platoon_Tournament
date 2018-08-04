# @thomasrw
# copyright 2018
#Methods to read in multiple tournament result_sets and analyze results

import pickle
import axelrod as axl

#TODO recover results
#Name convention players-run1 and run1
#Directory to find files
file_path = "/home/thomasrw/Desktop/platoon_tournament_results/"

def recover_results(p,r):
    file_path = p
    run_number = r

    with open(file_path + 'players-run' + str(run_number), 'rb') as handle:
        played = pickle.load(handle)
    myfile = file_path + 'run' + str(run_number)
    secondresults = axl.ResultSet(myfile, players=played, repetitions=10)
    #print(secondresults.ranked_names)
    return secondresults

#TODO determine key data to capture
#Max score by Strategy
#Game[] where Strategy_max achieved
#Max system score (cumulative of all strategies)
#Game[] where System_max achieved
#Total victor overall
#Max_system score (%) compared to Pareto Optimal, ie a platoon always forms

#TODO investigate matches vs tourney and how play(self) is counted
#TODO iterate over results capturing key data


print("Goliath online")

results = recover_results(file_path,1000)
print(results.ranked_names)

