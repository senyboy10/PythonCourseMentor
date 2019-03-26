"""

Author: ALSENY SYLLA

This code takes as input initial bunny population and initial fox population, then prints out the start population, end population, whether it 

"""
def next_pop(bpop, fpop): #calculates next year's bunny and fox populations
    bpop_next = max(0,int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop))
    fpop_next = max(0,int(0.4 * fpop + 0.02 * fpop * bpop))
    return (bpop_next, fpop_next)

def check_convergence(bpop, fpop): #checks if bunny and fox population converge or not, as well as where it ends
    i = 1
    blist = [bpop]  
    flist = [fpop]
    while i < 100:
        bpop_next, fpop_next = next_pop(blist[i-1], flist[i-1])
        blist.append(bpop_next)
        flist.append(fpop_next)
        
        if bpop == 0 or fpop == 0: 
            return (blist[i-1], flist[i-1], i, True)
        if bpop_next == 0 or fpop_next == 0:
            return (blist[i], flist[i], i+1, True)
        if bpop_next == blist[i-1] and fpop_next == flist[i-1]:
            return (blist[i], flist[i], i+1, True)
        if i == 99:
            return (blist[i], flist[i], i+1, False)
        i += 1
        

bpop = int(raw_input("Please enter the starting bunny population ==> "))
print bpop

fpop = int(raw_input("Please enter the starting fox population ==> "))
print fpop

four_tuple = check_convergence(bpop, fpop)

print "(Bunny, Fox): Start (" + str(bpop) + ", " + str(fpop) + ")  End: (" + str(four_tuple[0]) + "," + str(four_tuple[1]) + "), Converged: " + str(four_tuple[3]) + " in " + str(four_tuple[2]) + " generations"