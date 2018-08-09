# @thomasrw
# copyright 2018
#Methods to read in multiple tournament result_sets and analyze results

import pickle
import axelrod as axl
from axelrod.action import Action, str_to_actions
#import axelrod.interaction_utils as iu
#from . import eigen
#from .game import Game


C, D = Action.C, Action.D


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
#Max score by Strategy ... done
#Game[] where Strategy_max achieved ... done
#Max system score (cumulative of all strategies) ... done
#Game[] where System_max achieved ... done
#Total victor overall ... done
#Max_system score (%) compared to Pareto Optimal, ie a platoon always forms (250*49 = 12250) ... done

#normalized score by strategy eg sum score of 200 / 10 instances = 20 per instance --save for moran tourney
#Game[] where normalized max achieved --save for moran tourney

#TODO functions to store interim results that can be expanded later
#TODO iterate over results capturing key data


def get_avg_system_score(results):
    j=0
    for i in range(len(results.scores)):
        j += get_avg_score(results,i)
        #print(j)
    #print("avg sys score")
    #print(j)
    j = round(j,2) #rounding to drop floating point rounding garbage 12 digits past the decimal point
    return j

Max_System_Score = -1
Best_System_Runs = []
def update_max_system_score(results):
    global Max_System_Score
    global Run
    global Best_System_Runs
    c = get_avg_system_score(results)
    if c > Max_System_Score:
        Max_System_Score = c
        Best_System_Runs = [Run]
    elif c == Max_System_Score:
        Best_System_Runs.append(Run)


def get_avg_score(results, player_num):
    c = sum(z for z in results.scores[player_num]) / results.repetitions
    #print("c for " + str(player_num) + " is")
    #print(c)
    return c

strategies = [s() for s in axl.demo_strategies]
#[Cooperator, Defector, Tit For Tat, Grudger, Random: 0.5]
Max_Strategy_Scores = [0,0,0,0,0]
Sum_Strategy_Scores = [0,0,0,0,0]
#Best_Runs = [-1, -1, -1, -1, -1]
Best_Runs = [[] for x in range(5)]

#Max_Defector_Score = 0
#Max_Grudger_Score = 0
#Max_TitForTat_Score = 0
Max_Cooperator_Score = 0
#Max_Random_Score = 0
Run = 0

def update_max_scores(results):
    global Max_Strategy_Scores
    global Best_Runs
    global strategies
    global Run
    global Sum_Strategy_Scores
    for z in range(results.players.__len__()):
        #print(results.players[z])
        for y in range(len(strategies)):
            if str(results.players[z]) == str(strategies[y]):
                c = get_avg_score(results, z)
                Sum_Strategy_Scores[y] += c
                if c > Max_Strategy_Scores[y]:
                    Max_Strategy_Scores[y] = c

                    list = [Run]
                    Best_Runs[y] = list
                elif c == Max_Strategy_Scores[y]:
                    print("test")
                    Best_Runs[y].append(Run)



def update_max(results):
    global Max_Cooperator_Score
    for z in range(results.players.__len__()):
        print(results.players[z])
        if str(results.players[z]) == 'Cooperator':
            c = get_avg_score(results, z)
            if c > Max_Cooperator_Score:
                Max_Cooperator_Score = c


cooperative = [(C, D), (D, C), (C, C)]
print("Goliath online")

'''
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
'''
'''
for x in range(5):
    Run = x+1
    update_max_scores(recover_results(file_path,Run))
print(strategies)
print(Max_Strategy_Scores)
print(Best_Runs)
'''

'''
results = recover_results(file_path, 4000)
print(results.state_distribution)
print(len(results.state_distribution))
print(results.state_distribution[0])
print(results.state_distribution[0][0])

print(results.state_distribution[0][1])
print(results.state_distribution[0][1].keys())

k = list(results.state_distribution[0][1].keys())
print(k[0])

print(results.state_distribution[0][1].get(k[0]))


v = 0
for k in cooperative:
    try:
        v += results.state_distribution[0][1].get(k)
    except TypeError:
        print("oops")

print(results.state_distribution[0][1].get((C, C)))

print(v)
v = 0

def sum_state_distro(results, g):
    global cooperative
    v=0
    for i in range(len(results.state_distribution[g])):
        for k in cooperative:
            try:
                v += results.state_distribution[g][i].get(k)
            except TypeError:
                v=v #do nothing
    return v



#v = sum_state_distro(results)
print(v)

print(results.players)
print(results.state_distribution)

v=0
print(len(results.state_distribution))
for g in range(len(results.state_distribution)):
    v += sum_state_distro(results,g)
print(v)
print (v/500)

print(results.scores)

ou = get_avg_system_score(results)
print(ou)
'''


for x in range(13):
    Run = x+1
    results = recover_results(file_path, Run)
    update_max_scores(results)
    update_max_system_score(results)
print(strategies)
print(Sum_Strategy_Scores)
print(Max_Strategy_Scores)
print(Best_Runs)
print(Max_System_Score)
print(Best_System_Runs)

#Determine winning Strategy (static case)
z=0
zi=-1
for y in range(len(Sum_Strategy_Scores)):
    if z < Sum_Strategy_Scores[y]:
        z = Sum_Strategy_Scores[y]
        zi = y


#print(z)
print(strategies[zi])
print(Max_System_Score/(250*49))




