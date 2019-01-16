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
#file_path = "/home/thomasrw/Desktop/platoon_tournament_results/"
file_path = "/media/thomasrw/passport drive/tournament1/"

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

'''
for x in range(316251):
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
'''
best_runs = [1, 2, 3, 4, 5, 10, 11, 13, 26, 27, 29, 32, 56, 57, 59, 62, 66, 106, 107, 109, 112, 116, 121, 183, 184, 186, 189, 193, 198, 204, 295, 296, 298, 301, 305, 310, 316, 323, 451, 452, 454, 457, 461, 466, 472, 479, 487, 661, 662, 664, 667, 671, 676, 682, 689, 697, 706, 936, 937, 939, 942, 946, 951, 957, 964, 972, 981, 991, 1288, 1289, 1291, 1294, 1298, 1303, 1309, 1316, 1324, 1333, 1343, 1354, 1730, 1731, 1733, 1736, 1740, 1745, 1751, 1758, 1766, 1775, 1785, 1796, 1808, 2276, 2277, 2279, 2282, 2286, 2291, 2297, 2304, 2312, 2321, 2331, 2342, 2354, 2367, 2941, 2942, 2944, 2947, 2951, 2956, 2962, 2969, 2977, 2986, 2996, 3007, 3019, 3032, 3046, 3741, 3742, 3744, 3747, 3751, 3756, 3762, 3769, 3777, 3786, 3796, 3807, 3819, 3832, 3846, 3861, 4693, 4694, 4696, 4699, 4703, 4708, 4714, 4721, 4729, 4738, 4748, 4759, 4771, 4784, 4798, 4813, 4829, 5815, 5816, 5818, 5821, 5825, 5830, 5836, 5843, 5851, 5860, 5870, 5881, 5893, 5906, 5920, 5935, 5951, 5968, 7126, 7127, 7129, 7132, 7136, 7141, 7147, 7154, 7162, 7171, 7181, 7192, 7204, 7217, 7231, 7246, 7262, 7279, 7297, 8646, 8647, 8649, 8652, 8656, 8661, 8667, 8674, 8682, 8691, 8701, 8712, 8724, 8737, 8751, 8766, 8782, 8799, 8817, 8836, 10396, 10397, 10399, 10402, 10406, 10411, 10417, 10424, 10432, 10441, 10451, 10462, 10474, 10487, 10501, 10516, 10532, 10549, 10567, 10586, 10606, 12398, 12399, 12401, 12404, 12408, 12413, 12419, 12426, 12434, 12443, 12453, 12464, 12476, 12489, 12503, 12518, 12534, 12551, 12569, 12588, 12608, 12629, 14675, 14676, 14678, 14681, 14685, 14690, 14696, 14703, 14711, 14720, 14730, 14741, 14753, 14766, 14780, 14795, 14811, 14828, 14846, 14865, 14885, 14906, 14928, 17251, 17252, 17254, 17257, 17261, 17266, 17272, 17279, 17287, 17296, 17306, 17317, 17329, 17342, 17356, 17371, 17387, 17404, 17422, 17441, 17461, 17482, 17504, 17527, 20151, 20152, 20154, 20157, 20161, 20166, 20172, 20179, 20187, 20196, 20206, 20217, 20229, 20242, 20256, 20271, 20287, 20304, 20322, 20341, 20361, 20382, 20404, 20427, 20451, 23401, 23402, 23404, 23407, 23411, 23416, 23422, 23429, 23437, 23446, 23456, 23467, 23479, 23492, 23506, 23521, 23537, 23554, 23572, 23591, 23611, 23632, 23654, 23677, 23701, 23726, 27028, 27029, 27031, 27034, 27038, 27043, 27049, 27056, 27064, 27073, 27083, 27094, 27106, 27119, 27133, 27148, 27164, 27181, 27199, 27218, 27238, 27259, 27281, 27304, 27328, 27353, 27379, 31060, 31061, 31063, 31066, 31070, 31075, 31081, 31088, 31096, 31105, 31115, 31126, 31138, 31151, 31165, 31180, 31196, 31213, 31231, 31250, 31270, 31291, 31313, 31336, 31360, 31385, 31411, 31438, 35526, 35527, 35529, 35532, 35536, 35541, 35547, 35554, 35562, 35571, 35581, 35592, 35604, 35617, 35631, 35646, 35662, 35679, 35697, 35716, 35736, 35757, 35779, 35802, 35826, 35851, 35877, 35904, 35932, 40456, 40457, 40459, 40462, 40466, 40471, 40477, 40484, 40492, 40501, 40511, 40522, 40534, 40547, 40561, 40576, 40592, 40609, 40627, 40646, 40666, 40687, 40709, 40732, 40756, 40781, 40807, 40834, 40862, 40891, 45881, 45882, 45884, 45887, 45891, 45896, 45902, 45909, 45917, 45926, 45936, 45947, 45959, 45972, 45986, 46001, 46017, 46034, 46052, 46071, 46091, 46112, 46134, 46157, 46181, 46206, 46232, 46259, 46287, 46316, 46346, 51833, 51834, 51836, 51839, 51843, 51848, 51854, 51861, 51869, 51878, 51888, 51899, 51911, 51924, 51938, 51953, 51969, 51986, 52004, 52023, 52043, 52064, 52086, 52109, 52133, 52158, 52184, 52211, 52239, 52268, 52298, 52329, 58345, 58346, 58348, 58351, 58355, 58360, 58366, 58373, 58381, 58390, 58400, 58411, 58423, 58436, 58450, 58465, 58481, 58498, 58516, 58535, 58555, 58576, 58598, 58621, 58645, 58670, 58696, 58723, 58751, 58780, 58810, 58841, 58873, 65451, 65452, 65454, 65457, 65461, 65466, 65472, 65479, 65487, 65496, 65506, 65517, 65529, 65542, 65556, 65571, 65587, 65604, 65622, 65641, 65661, 65682, 65704, 65727, 65751, 65776, 65802, 65829, 65857, 65886, 65916, 65947, 65979, 66012, 73186, 73187, 73189, 73192, 73196, 73201, 73207, 73214, 73222, 73231, 73241, 73252, 73264, 73277, 73291, 73306, 73322, 73339, 73357, 73376, 73396, 73417, 73439, 73462, 73486, 73511, 73537, 73564, 73592, 73621, 73651, 73682, 73714, 73747, 73781, 81586, 81587, 81589, 81592, 81596, 81601, 81607, 81614, 81622, 81631, 81641, 81652, 81664, 81677, 81691, 81706, 81722, 81739, 81757, 81776, 81796, 81817, 81839, 81862, 81886, 81911, 81937, 81964, 81992, 82021, 82051, 82082, 82114, 82147, 82181, 82216, 90688, 90689, 90691, 90694, 90698, 90703, 90709, 90716, 90724, 90733, 90743, 90754, 90766, 90779, 90793, 90808, 90824, 90841, 90859, 90878, 90898, 90919, 90941, 90964, 90988, 91013, 91039, 91066, 91094, 91123, 91153, 91184, 91216, 91249, 91283, 91318, 91354, 100530, 100531, 100533, 100536, 100540, 100545, 100551, 100558, 100566, 100575, 100585, 100596, 100608, 100621, 100635, 100650, 100666, 100683, 100701, 100720, 100740, 100761, 100783, 100806, 100830, 100855, 100881, 100908, 100936, 100965, 100995, 101026, 101058, 101091, 101125, 101160, 101196, 101233, 111151, 111152, 111154, 111157, 111161, 111166, 111172, 111179, 111187, 111196, 111206, 111217, 111229, 111242, 111256, 111271, 111287, 111304, 111322, 111341, 111361, 111382, 111404, 111427, 111451, 111476, 111502, 111529, 111557, 111586, 111616, 111647, 111679, 111712, 111746, 111781, 111817, 111854, 111892, 122591, 122592, 122594, 122597, 122601, 122606, 122612, 122619, 122627, 122636, 122646, 122657, 122669, 122682, 122696, 122711, 122727, 122744, 122762, 122781, 122801, 122822, 122844, 122867, 122891, 122916, 122942, 122969, 122997, 123026, 123056, 123087, 123119, 123152, 123186, 123221, 123257, 123294, 123332, 123371, 134891, 134892, 134894, 134897, 134901, 134906, 134912, 134919, 134927, 134936, 134946, 134957, 134969, 134982, 134996, 135011, 135027, 135044, 135062, 135081, 135101, 135122, 135144, 135167, 135191, 135216, 135242, 135269, 135297, 135326, 135356, 135387, 135419, 135452, 135486, 135521, 135557, 135594, 135632, 135671, 135711, 148093, 148094, 148096, 148099, 148103, 148108, 148114, 148121, 148129, 148138, 148148, 148159, 148171, 148184, 148198, 148213, 148229, 148246, 148264, 148283, 148303, 148324, 148346, 148369, 148393, 148418, 148444, 148471, 148499, 148528, 148558, 148589, 148621, 148654, 148688, 148723, 148759, 148796, 148834, 148873, 148913, 148954, 162240, 162241, 162243, 162246, 162250, 162255, 162261, 162268, 162276, 162285, 162295, 162306, 162318, 162331, 162345, 162360, 162376, 162393, 162411, 162430, 162450, 162471, 162493, 162516, 162540, 162565, 162591, 162618, 162646, 162675, 162705, 162736, 162768, 162801, 162835, 162870, 162906, 162943, 162981, 163020, 163060, 163101, 163143, 177376, 177377, 177379, 177382, 177386, 177391, 177397, 177404, 177412, 177421, 177431, 177442, 177454, 177467, 177481, 177496, 177512, 177529, 177547, 177566, 177586, 177607, 177629, 177652, 177676, 177701, 177727, 177754, 177782, 177811, 177841, 177872, 177904, 177937, 177971, 178006, 178042, 178079, 178117, 178156, 178196, 178237, 178279, 178322, 193546, 193547, 193549, 193552, 193556, 193561, 193567, 193574, 193582, 193591, 193601, 193612, 193624, 193637, 193651, 193666, 193682, 193699, 193717, 193736, 193756, 193777, 193799, 193822, 193846, 193871, 193897, 193924, 193952, 193981, 194011, 194042, 194074, 194107, 194141, 194176, 194212, 194249, 194287, 194326, 194366, 194407, 194449, 194492, 194536, 210796, 210797, 210799, 210802, 210806, 210811, 210817, 210824, 210832, 210841, 210851, 210862, 210874, 210887, 210901, 210916, 210932, 210949, 210967, 210986, 211006, 211027, 211049, 211072, 211096, 211121, 211147, 211174, 211202, 211231, 211261, 211292, 211324, 211357, 211391, 211426, 211462, 211499, 211537, 211576, 211616, 211657, 211699, 211742, 211786, 211831, 229173, 229174, 229176, 229179, 229183, 229188, 229194, 229201, 229209, 229218, 229228, 229239, 229251, 229264, 229278, 229293, 229309, 229326, 229344, 229363, 229383, 229404, 229426, 229449, 229473, 229498, 229524, 229551, 229579, 229608, 229638, 229669, 229701, 229734, 229768, 229803, 229839, 229876, 229914, 229953, 229993, 230034, 230076, 230119, 230163, 230208, 230254, 248725, 248726, 248728, 248731, 248735, 248740, 248746, 248753, 248761, 248770, 248780, 248791, 248803, 248816, 248830, 248845, 248861, 248878, 248896, 248915, 248935, 248956, 248978, 249001, 249025, 249050, 249076, 249103, 249131, 249160, 249190, 249221, 249253, 249286, 249320, 249355, 249391, 249428, 249466, 249505, 249545, 249586, 249628, 249671, 249715, 249760, 249806, 249853, 269501, 269502, 269504, 269507, 269511, 269516, 269522, 269529, 269537, 269546, 269556, 269567, 269579, 269592, 269606, 269621, 269637, 269654, 269672, 269691, 269711, 269732, 269754, 269777, 269801, 269826, 269852, 269879, 269907, 269936, 269966, 269997, 270029, 270062, 270096, 270131, 270167, 270204, 270242, 270281, 270321, 270362, 270404, 270447, 270491, 270536, 270582, 270629, 270677, 291551, 291552, 291554, 291557, 291561, 291566, 291572, 291579, 291587, 291596, 291606, 291617, 291629, 291642, 291656, 291671, 291687, 291704, 291722, 291741, 291761, 291782, 291804, 291827, 291851, 291876, 291902, 291929, 291957, 291986, 292016, 292047, 292079, 292112, 292146, 292181, 292217, 292254, 292292, 292331, 292371, 292412, 292454, 292497, 292541, 292586, 292632, 292679, 292727, 292776, 314926, 314927, 314929, 314932, 314936, 314941, 314947, 314954, 314962, 314971, 314981, 314992, 315004, 315017, 315031, 315046, 315062, 315079, 315097, 315116, 315136, 315157, 315179, 315202, 315226, 315251, 315277, 315304, 315332, 315361, 315391, 315422, 315454, 315487, 315521, 315556, 315592, 315629, 315667, 315706, 315746, 315787, 315829, 315872, 315916, 315961, 316007, 316054, 316102, 316151, 316201]



total_players = 0
num_cooperator = 0
num_defector = 0
num_titfortat = 0
num_grudger = 0
num_random = 0

for x in range(1):#best_runs:
    Run = 15
    results = recover_results(file_path, Run)
    for y in range(len(results.players)):
        if str(results.players[y]) == "Cooperator":
            num_cooperator += 1
        if str(results.players[y]) == "Defector":
            num_defector += 1
        if str(results.players[y]) == "Tit For Tat":
            num_titfortat += 1
        if str(results.players[y]) == "Grudger":
            num_grudger += 1
        if str(results.players[y]) == "Random: 0.5":
            num_random += 1
        total_players += 1
    #print(results.ranked_names)
    #print(count(results.players))
print(Run)
print(total_players)
print(num_cooperator)
print(num_defector)
print(num_titfortat)
print(num_grudger)
print(num_random)



