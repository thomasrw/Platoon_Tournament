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

#TODO investigate matches vs tourney and how play(self) is counted? - or account for it in results analysis
#TODO iterate over results capturing key data


def get_avg_score(results, player_num):
    c = sum(z for z in results.scores[player_num]) / results.repetitions
    return c

strategies = [s() for s in axl.demo_strategies]
#[Cooperator, Defector, Tit For Tat, Grudger, Random: 0.5]
Max_Strategy_Scores = [0,0,0,0,0]
Best_Runs = [-1, -1, -1, -1, -1]

#Max_Defector_Score = 0
#Max_Grudger_Score = 0
#Max_TitForTat_Score = 0
Max_Cooperator_Score = 0
#Max_Random_Score = 0


def update_max_scores(results):
    global Max_Strategy_Scores
    global strategies
    for z in range(results.players.__len__()):
        #print(results.players[z])
        for y in range(len(strategies)):
            if str(results.players[z]) == str(strategies[y]):
                c = get_avg_score(results, z)
                if c > Max_Strategy_Scores[y]:
                    Max_Strategy_Scores[y] = c
                    # TODO reset best run list and add run that the max score was achieved in
                elif c == Max_Strategy_Scores[y]:
                    print("test")

                    #TODO append run to list of runs that max score was achieved in



def update_max(results):
    global Max_Cooperator_Score
    for z in range(results.players.__len__()):
        print(results.players[z])
        if str(results.players[z]) == 'Cooperator':
            c = get_avg_score(results, z)
            if c > Max_Cooperator_Score:
                Max_Cooperator_Score = c



print("Goliath online")

results = recover_results(file_path,2)
print(results.ranked_names)
print(results.players)
print(results.players[0])
print(results.scores)
print(results.scores[49])


print( get_avg_score(results, 0))
print(results.players.__len__())

print(results.repetitions)

print(Max_Cooperator_Score)
update_max(results)
print(Max_Cooperator_Score)

print(strategies)
update_max_scores(results)
print(Max_Strategy_Scores)
update_max_scores(results)

for x in range(10):
    update_max_scores(recover_results(file_path,x+1))
print(strategies)
print(Max_Strategy_Scores)
print(Best_Runs)
