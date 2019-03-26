"""

Author: ALSENY SYLLA
This code takes as input a country, and lists all the games it played in during the 2014 FIFA World Cup, as well as the winner of each game. Then, it lists the stats of the team, including amount of games played, wins, losses, draws, goals forward, and goals against, then the highest achievement of this team. If the team placed in the top four, the program prints what place the team was.

"""
import hw4_util
results = hw4_util.read_games('all_games.txt')

team = raw_input("Please enter a country ==> ")
print team

team = team.lower()

print "All games: "

i = 0
wins = 0
games = 0
draw = 0
lose = 0
gf = 0
ga = 0
j = 0

while i < len(results):
    if results[i][0].lower() == team or results[i][2].lower() == team:
        print results[i][0].rjust(24) + str(results[i][1]).rjust(4) + "-" + str(results[i][3]).ljust(4) + results[i][2].ljust(24) + "Winner:" + results[i][4]
        
        j = i + 1
        
        games += 1
        if results[i][0].lower() == team:
            gf += results[i][1]
            ga += results[i][3]
        elif results[i][2].lower() == team:
            ga += results[i][1]
            gf += results[i][3] 
        
        if results[i][4].lower() == team:
            wins += 1
        elif results[i][4].lower() == "draw":
            draw += 1
        else:
            lose += 1
        
    i += 1
    
    
print "Scores: \n" + "Games".ljust(6) + "Win".ljust(6) + "Lose".ljust(6) + "Draw".ljust(6) + "GF".ljust(6) + "GA".ljust(6)
print str(games).ljust(6) + str(wins).ljust(6) + str(lose).ljust(6) + str(draw).ljust(6) + str(gf).ljust(6) + str(ga).ljust(6)

if j <= 48 and j > 0:
    print "The highest achievement in 2014 World cup was group games"
elif j > 48 and j <= 56:
    print "The highest achievement in 2014 World cup was round of 16"
elif j > 56 and j <= 60:
    print "The highest achievement in 2014 World cup was quarter finals"
elif j > 60 and j <= 62:
    print "The highest achievement in 2014 World cup was semi finals"
elif j == 63:
    print "The highest achievement in 2014 World cup was the third place playoff"
    if results[j-1][4].lower() == team:
        print "This country placed in the third place"
    else:
        print "This country placed in the fourth place"
elif j == 64:
    print "The highest achievement in 2014 World cup was finals"
    if results[j-1][4].lower() == team:
        print "This country placed in the first place"
    else:
        print "This country placed in the second place"
else:
    print "The highest achievement in 2014 World cup was not making it to the tournament"