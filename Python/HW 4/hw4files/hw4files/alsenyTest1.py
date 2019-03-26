import hw4_util 
results = hw4_util.read_games('all_games.txt') 

selectCountry = input("Please enter a country ==> ")
print (selectCountry)


listAllGamesPlayed = []
win = 0
lose = 0
draw = 0
gf = 0
ga = 0
games = 0
highestLevel = 0;

def gamePlayed(CurrentList, country ):
	for x in CurrentList:
		if (country.casefold() == CurrentList[0].casefold() or country.casefold() == CurrentList[2].casefold()):
			global games
			global gf
			global ga
			global win
			global draw
			global lose
			

			games += 1
			if(CurrentList[0].casefold()== country.casefold()):

				gf += CurrentList[1]
				ga += CurrentList[3]
			elif(CurrentList[2].casefold()== country.casefold()):
				gf += CurrentList[3]
				ga += CurrentList[1]


			if(CurrentList[4].casefold()==country.casefold()):
				win += 1
			elif CurrentList[4].casefold()== "Draw".casefold():
				draw += 1
			else: 
				lose += 1
			

			return True;
	return False

count = 0
for x in results:
	count += 1
	if gamePlayed(x, selectCountry):
		highestLevel = 1 + count
		listAllGamesPlayed.append(x)

def printGames():
	print("All games:")
	for x in listAllGamesPlayed:
		print(x[0].rjust(24) + str(x[1]).rjust(4)+ "-"+ str(x[3]).ljust(4)+ x[2].ljust(24)+"winner:"+x[4])


printGames()
print(win, lose, draw, gf, ga , highestLevel)