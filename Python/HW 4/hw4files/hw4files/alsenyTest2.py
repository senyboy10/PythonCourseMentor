
import hw4_util 
medals2010 = hw4_util.read_medals('medals2010.txt') 
medals2014 = hw4_util.read_medals('medals2014.txt')

selectCountry = input("Enter the name of a country ==> ")
print(selectCountry)
table = ("Year".ljust(8)+ "Country".ljust(14)+ "Gold".rjust(8)+"Silver".rjust(8)+"Bronze".rjust(8)+"Total".rjust(8))
print(table)
print("="*len(table))

# 
def totalMedals(medalsXXXX):
	totals = list((0,0,0,0))
	for x in medalsXXXX: 
		#gold
		totals[0] += x[1]
		#silver
		totals[1] += x[2]
		#Bronze
		totals[2] += x[3]
		#Total
		totals[3] += x[4]

	return totals

def findCountry(medalsXXXX, country):
	currCountry = []

	for x in medalsXXXX:
		
		if (x[0].casefold()== country.casefold()):
			return x

	return currCountry

def findPercentage(country, medals):
	c = findCountry(medals, country)
	if(len(c)!=0):
		t = totalMedals(medals)
		return [int(100*float(c[1])/float(t[0])),
				int(100*float(c[2])/float(t[1])),
				int(100*float(c[3])/float(t[2])),
				int(100*float(c[4])/float(t[3]))]
	return []

			




def printOutput(selectCountry, medals, year):
	cStats = findPercentage(selectCountry, medals)
	if(cStats):
		print(year.ljust(8)+ selectCountry.capitalize().ljust(14)+ 
			(str(cStats[0])+("%")).rjust(8)+(str(cStats[1])+"%").rjust(8)+
			(str(cStats[2])+"%").rjust(8)+(str(cStats[3])+"%").rjust(8))

printOutput(selectCountry, medals2010, "2010")
printOutput("united states", medals2010, "2010")
print()
printOutput(selectCountry, medals2014, "2014")
printOutput("united states", medals2014, "2014")