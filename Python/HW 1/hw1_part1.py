
#code calculates percentage change of number of posts of two hashtags

##function returns percent increase of two values, x1 and x2
def pctinc(x1,x2):
    pctinc = ((x2 - x1) / x1) * 100
    return pctinc

print "#icebucketchallenge vs #alsicebucketchallenge, percent change"

ibc_pctinc_1 = pctinc(200.,500)
alsibc_pctinc_1 = pctinc(100.,300)
    
print int(ibc_pctinc_1), "vs", int(alsibc_pctinc_1)

ibc_pctinc_2 = pctinc(500.,2000)
alsibc_pctinc_2 = pctinc(300.,1500)
    
print int(ibc_pctinc_2), "vs", int(alsibc_pctinc_2)

ibc_pctinc_3 = pctinc(2000.,12000)
alsibc_pctinc_3 = pctinc(1500.,13000)
    
print int(ibc_pctinc_3), "vs", int(alsibc_pctinc_3)

ibc_pctinc_4 = pctinc(12000.,24000)
alsibc_pctinc_4 = pctinc(13000.,25000)
    
print int(ibc_pctinc_4), "vs", int(alsibc_pctinc_4)

ibc_pctinc_5 = pctinc(24000.,65000)
alsibc_pctinc_5 = pctinc(25000.,105000)
    
print int(ibc_pctinc_5), "vs", int(alsibc_pctinc_5)

ibc_pctinc_6 = pctinc(65000.,70000)
alsibc_pctinc_6 = pctinc(105000.,85000)
    
print int(ibc_pctinc_6), "vs", int(alsibc_pctinc_6)
