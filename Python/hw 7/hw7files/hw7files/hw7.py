"""

Author: ALSENY SYLLA
R

This code takes as input two files with a list of birds and pigs, and then runs a simulation similar to the game 'Angry Birds', and prints out the times when pigs are popped,
speed is reduced, etc.

"""

from Bird import *
from Pig import *
    
if __name__ == '__main__':

    bird = raw_input("Enter the name of the birds file ==> ")
    print bird
    
    pig = raw_input("Enter the name of the pigs file ==> ")
    print pig
    
    print_birds = []
    birds = []
    for line in open(bird):
        l = line.split("|")
        print_birds.append(l[0] + " (%.1f,%.1f)"%(float(l[1]),float(l[2])))
        birds.append(Bird(l[0],l[1],l[2],l[3],l[4],l[5]))
    print "\nNum birds %d:"%(len(print_birds))
    
    for i in range(len(print_birds)):
        print print_birds[i]
    
    print "." * 4
    
    print_pigs = []
    pigs = []
    for line in open(pig):
        l = line.split("|")
        print_pigs.append(l[0] + " (%.1f,%.1f)"%(float(l[1]), float(l[2])))
        pigs.append(Pig(l[0],l[1],l[2],l[3]))
    print "Num pigs %d:"%(len(print_pigs))
    
    for i in range(len(print_pigs)):
        print print_pigs[i]
        
    print "." * 4
    birds_gone = []
    pigs_copy = pigs[:]
    t = 0
    
    for i in range(len(birds)):
        if len(pigs) == 0:
            break
    
        print "Time %d: %s starts at (%.1f,%.1f)"%(t, birds[i].name, float(birds[i].x), float(birds[i].y))
        
        while True:
            t += 1
            birds[i].move()
            
            j = 0
            while j < len(pigs):
                if birds[i].check_intersect(pigs[j]):
                    print "Time %d: %s at (%.1f,%.1f) has popped %s"%(t, birds[i].name, float(birds[i].x), float(birds[i].y), pigs[j].name)
                    birds[i].change_speed()
                    print "Time %d: %s at (%.1f,%.1f) now has (dx,dy) = (%.1f,%.1f)"%(t, birds[i].name, float(birds[i].x), float(birds[i].y), float(birds[i].dx), float(birds[i].dy))
                    pigs.remove(pigs[j])
                else:
                    j += 1
                
            if birds[i].min_speed():
                birds_gone.append(birds[i])
                print "Time %d: %s at location (%.1f,%.1f) with speed %.1f stops"%(t, birds[i].name, float(birds[i].x), float(birds[i].y), math.sqrt(birds[i].dx**2 + birds[i].dy**2))
                if len(birds) > 0 and len(pigs) > 0:
                    break
                
            if birds[i].check_boundary():
                birds_gone.append(birds[i])
                print "Time %d: %s at location (%.1f,%.1f) has left the game"%(t, birds[i].name, float(birds[i].x), float(birds[i].y))
                if len(birds) > 0 and len(pigs) > 0:                
                    break
                
            if len(pigs) == 0:
                break
     
    if len(pigs) == 0:
        print "Time %d: All pigs popped. The birds win!"%(t)
    elif len(birds_gone) == len(birds):
        print "Time %d: No more birds. The pigs win!\nRemaining pigs:"%(t)
        for pig in pigs:
            print pig.name    