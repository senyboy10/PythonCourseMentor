
import hw4_util

def print_percentage(year, medals, totals, country): #this function calculates the percentage of medals that a country has won for either 2010 or 2014, depending on the input
    i = 0
     
    while i < len(medals):
        if country.lower() == medals[i][0].lower():
            gold = int(medals[i][1] / float(totals[0]) * 100)
            silver = int(medals[i][2] / float(totals[1]) * 100)
            bronze = int(medals[i][3] / float(totals[2]) * 100)
            total = int(medals[i][4] / float(totals[3]) * 100)
            
            print year.ljust(8) + (country).ljust(14) + (str(gold) + "%").rjust(8) + (str(silver) + "%").rjust(8) + (str(bronze) + "%").rjust(8) + (str(total) + "%").rjust(8)
        i += 1


medals2010 = hw4_util.read_medals('medals2010.txt')
medals2014 = hw4_util.read_medals('medals2014.txt')

country = raw_input("Enter the name of a country ==> ")
print country

i = 0
j = 0
totals2010 = [0,0,0,0]
totals2014 = [0,0,0,0]

while i < len(medals2010):
    totals2010[0] += medals2010[i][1]
    totals2010[1] += medals2010[i][2]
    totals2010[2] += medals2010[i][3]
    totals2010[3] += medals2010[i][4]
    i += 1

while j < len(medals2014):
    totals2014[0] += medals2014[j][1]
    totals2014[1] += medals2014[j][2]
    totals2014[2] += medals2014[j][3]
    totals2014[3] += medals2014[j][4]
    j += 1
    

mystr = "Year".ljust(8) + "Country".ljust(14) + "Gold".rjust(8) + "Silver".rjust(8) + "Bronze".rjust(8) + "Total".rjust(8)
print mystr
print "=" * len(mystr)

print_percentage('2010', medals2010, totals2010, country)
print_percentage('2010', medals2010, totals2010, 'United States')
print
print_percentage('2014', medals2014, totals2014, country)
print_percentage('2014', medals2014, totals2014, 'United States')

