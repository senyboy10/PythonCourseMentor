"""

Author: ALSENY SYLLA

This code takes as input two numbers which refer to an index of soccer teams, and then outputs the standings of the two teams and which team is better by using the same methodology as FIFA. 

"""

import hw3_util

def print_info(team): #this function extracts info about group, team name, number of wins, draws, and losses, goals forward and against, calculates the goal difference and points, and then prints this
    group = str(team[0])
    t = str(team[1])
    win = str(team[3])
    draw = str(team[4])
    lose = str(team[5])
    gf = str(team[6])
    ga = str(team[7])
    gdiff = str(int(gf) - int(ga))
    pts = str((3 * int(win)) + int(draw))
    print group.ljust(6) + t.ljust(20) + win.ljust(6) + draw.ljust(6) + lose.ljust(6) + gf.ljust(6) + ga.ljust(6) + gdiff.ljust(6) + pts.ljust(6)
    
def points(team): #returns the points value of a team
    win = team[3]
    draw = team[4]  
    pts = (3 * win) + draw
    return pts

def name(team): #returns a team's name
    return team[1]

def gd(team): #calculates and returns a team's goal difference
    return team[6] - team[7]

def gs(team): #returns goals scored for a team
    return team[6]



teams = hw3_util.read_fifa()

index1 = int(raw_input("First team index (0-31) ==> "))
print index1

index2 = int(raw_input("Second team index (0-31) ==> "))
print index2

g = "Group"
t = "Team"
w = "Win"
d = "Draw"
l = "Lose"
gf = "GF"
ga = "GA"
gdiff = "Gdiff"
p = "Pts"

g = g.ljust(6)
t = t.ljust(20)
w = w.ljust(6)
d = d.ljust(6)
l = l.ljust(6)
gf = gf.ljust(6)
ga = ga.ljust(6)
gdiff = gdiff.ljust(6)
p = p.ljust(6)

print "\n" + g + t + w + d + l + gf + ga + gdiff + p
print_info(teams[index1])
print_info(teams[index2])

t1 = name(teams[index1])
t2 = name(teams[index2])
p1 = points(teams[index1])
p2 = points(teams[index2])
gd1 = gd(teams[index1])
gd2 = gd(teams[index2])
gs1 = gs(teams[index1])
gs2 = gs(teams[index2])

if p1 > p2:
    print t1, "is better than", t2 
elif p2 > p1:
    print t2, "is better than", t1
elif gd1 > gd2: #points are equal 
    print t1, "is better than", t2
elif gd2 > gd1:
    print t2, "is better than", t1
elif gs1 > gs2: #GDs are equal
    print t1, "is better than", t2
elif gs2 > gs1:
    print t2, "is better than", t1
else:
    print t2, "same as", t1