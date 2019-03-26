"""

Author: ALSENY SYLLA

This code takes as input the stats of two teams, and then outputs a table that tells someone which team will be ahead after the next game played depending on the game's score

"""
def winner(team1, team2, score): #calculates which team comes out ahead based on what the game score is and the stats of the two teams
    team1 = team1.split(",")
    team2 = team2.split(",")
    
    p1 = int(team1[0])*3 + int(team1[2])
    p2 = int(team2[0])*3 + int(team2[2])
    gs1 = int(team1[3])
    gs2 = int(team2[3])
    ga1 = int(team1[4])
    ga2 = int(team2[4])
    
    score_list = score.split("-")
    
    gs1 += int(score_list[0])
    gs2 += int(score_list[1])
    
    ga1 += int(score_list[1])
    ga2 += int(score_list[0])
    
    gd1 = gs1 - ga1
    gd2 = gs2 - ga2
    
    if int(score_list[0]) > int(score_list[1]):
        p1 += 3
    elif int(score_list[1]) > int(score_list[0]):
        p2 += 3
    else:
        p1 += 1
        p2 += 1
    
    if p1 > p2:
        return "1"
    elif p2 > p1:
        return "2"
    elif gd1 > gd2:
        return "1"
    elif gd2 > gd1:
        return "2"
    elif gs1 > gs2:
        return "1"
    elif gs2 > gs1:
        return "2"
    else:
        return "0"


team1 = raw_input("Enter team 1 stats ==> ")
print team1

team2 = raw_input("Enter team 2 stats ==> ")
print team2

print "Columns are team 1 goals, rows are team 2 goals"

line1 = " " + "0".ljust(5) + " " + "1".ljust(5) + " " + "2".ljust(5) + " " + "3".ljust(5) + " " + "4".ljust(5)
print "Goals".center(5) + "|".center(3) + line1
print "-" * 6 + "|".center(1) + "-" * len(line1)

for i in range(5):
    print str(i).center(5)+ "|".center(3),
    for j in range(5):
        score = str(j) + "-" + str(i)
        print winner(team1, team2, score).ljust(5),
    print