
#code determines component score, spread, and total score of an olympic figure skater

short1 = 21
short2 = 32
short3 = 28
short4 = 24
short5 = 29

free1 = 24
free2 = 28
free3 = 19
free4 = 23
free5 = 24

print "Short program scores", short1, short2, short3, short4, short5
print "Free skating scores", free1, free2, free3, free4, free5

smaxplusmin = max(short1, short2, short3, short4, short5) + min(short1, short2, short3, short4, short5)
shortspread = (max(short1, short2, short3, short4, short5) - min(short1, short2, short3, short4, short5)) / (((short1 + short2 + short3 + short4 + short5) - smaxplusmin) / 3.)

fmaxplusmin = max(free1, free2, free3, free4, free5) + min(free1, free2, free3, free4, free5)
freespread = (max(free1, free2, free3, free4, free5) - min(free1, free2, free3, free4, free5)) / (((free1 + free2 + free3 + free4 + free5) - fmaxplusmin) / 3.)

print "Spread of the short program is", shortspread
print "Spread of the free skating is", freespread


shortscore = (short1 + short2 + short3 + short4 + short5) - (max(short1, short2, short3, short4, short5) + min(short1, short2, short3, short4, short5))
freescore = (free1 + free2 + free3 + free4 + free5) - (max(free1, free2, free3, free4, free5) + min(free1, free2, free3, free4, free5))

print "Total score for the short program is", shortscore
print "Total score for the free skating is", freescore


totalscore = shortscore + freescore

print "The total score for the competitor is", totalscore