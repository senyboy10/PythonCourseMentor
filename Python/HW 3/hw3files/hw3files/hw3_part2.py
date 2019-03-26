"""

Author: ALSENY SYLLA

This code takes as input the type of lego the user needs as well as how many pieces the user needs, and prints to the user how this lego can be formed, reading from a text file that has a list of legos available.

"""

import hw3_util

user_lego = raw_input("What type of lego do you need? ==> ")
print user_lego

num = int(raw_input("How many pieces of this lego do you need? ==> "))
print num

legos = hw3_util.read_legos('legos.txt')

if user_lego == '1x1' and num <= legos.count('1x1'):
    print "I have %d pieces of %s for this" %(num, user_lego)
elif user_lego == '1x1' and num > legos.count('1x1'):
    print "I don't have enough pieces for this lego"
elif user_lego == '2x1' and num <= legos.count('2x1'):
    print "I have %d pieces of %s for this" %(num, user_lego)
elif user_lego == '2x1' and num > legos.count('2x1'):
    num *= 2
    if legos.count('1x1') >= num:
        print "I have %d pieces of 1x1 for this" %(num)
    else:
        print "I don't have enough pieces for this lego"
elif user_lego == '2x2' and num <= legos.count('2x2'):
    print "I have %d pieces of %s for this" %(num, user_lego)
elif user_lego == '2x2' and num > legos.count('2x2'):
    num *= 2
    if legos.count('2x1') >= num:
        print "I have %d pieces of 2x1 for this" %(num)
    elif legos.count('2x1') < num:
        num *= 2
        if legos.count('1x1') >= num:
            print "I have %d pieces of 1x1 for this" %(num)
        else:
            print "I don't have enough pieces for this lego"            
elif user_lego == '2x4' and num <= legos.count('2x4'):
    print "I have %d pieces of %s for this" %(num, user_lego)
elif user_lego == '2x4' and num > legos.count('2x4'):
    num *= 2
    if legos.count('2x2') >= num:
        print "I have %d pieces of 2x2 for this" %(num)
    elif legos.count('2x2') < num:
        num *= 2
        if legos.count('2x1') >= num:
            print "I have %d pieces of 2x1 for this" %(num)
        elif legos.count('2x1') < num:
            num *= 2
            if legos.count('1x1') >= num:
                print "I have %d pieces of 1x1 for this" %(num)
            else:
                print "I don't have enough pieces for this lego"