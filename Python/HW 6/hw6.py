"""
Author: ALSENY SYLLA

This code assumes the existence of the file 'DrWhoVillains.tsv' and displays top 10 most popular villains, takes the user input to select one of those 10, and then displays what stories it is in with other villains and if there are stories with just that villain.
"""
import textwrap
    
def printtop10(f): #takes as input a file and displays top 10 most popular villains
    f = open(f)
    lc = []
    for line in f:
        line = line.split("\t")
        storystr = line[8].replace("\n", "").split(",")
        storystr = [story.strip() for story in storystr]
        storyset = set(storystr)
        lc.append((len(storyset), line[0]))
    
    lc.sort(reverse=True)
    print "\n1. %s \n2. %s \n3. %s \n4. %s \n5. %s \n6. %s \n7. %s \n8. %s \n9. %s \n10. %s" \
    %(lc[0][1], lc[1][1], lc[2][1], lc[3][1], lc[4][1], lc[5][1], lc[6][1], lc[7][1], lc[8][1], lc[9][1])

def printoutput(f, n): #prints the villains that are in stories with a given villain 'n' and the stories the villain is in by itself
    f = open(f)
    l = []
    stories = set([])
    for line in f:
        line = line.split("\t")
        storystr = line[8].replace("\n", "").split(",")   
        storystr = [story.strip() for story in storystr]       
        storyset = set(storystr)
        l.append((len(storyset), line[0], storyset))
    f.close()
    l.sort(reverse=True)
    
    for line in open('DrWhoVillains.tsv'):
        line = line.split("\t")
        storystr = line[8].replace("\n", "").split(",")   
        storystr = [story.strip() for story in storystr]       
        storyset = set(storystr)
        if l[n-1][1] == line[0]:
            continue
        for story in storystr:
            stories.add(story)
        
    l.sort(reverse=True)
    print "%s in %d stories, with the following other villains:\n" %(l[n-1][1], l[n-1][0]) + "=" * 50
    i = 0
    v = []
    while i < len(l):
        if len(l[i][2] & l[n-1][2]) != 0 and l[i][1] != l[n-1][1]:
            v.append(l[i][1])
        if l[n-1][1] == l[i][1]:
            s = l[n-1][2]
        i += 1
    print s
    print sorted(stories)
    only_stories = s - stories
    print only_stories
    v.sort()
    only_stories = sorted(only_stories)
    v_str = ""
    os_str = ""
    
    for vil in v:
        v_str += vil + ", "
    for story in only_stories:
        os_str += story + ", "
        
    v_str = v_str[:-2]
    os_str = os_str[:-2]
    for item in textwrap.wrap(v_str, 75):
        print " " * 5 + item
    
    if len(only_stories) != 0:
        print "\nThe stories that only features %s are:\n" %(l[n-1][1]) + "=" * 50
        for s in textwrap.wrap(os_str, 75):
            print " " * 5 + s
    else:
        print "\nThere are no stories with only this villain\n" + "=" * 50
        
    
if __name__ == '__main__':    
    while True:
        printtop10('DrWhoVillains.tsv')
        num = raw_input("Please enter a number between 1 and 10, or -1 to end \nEnter a villain ==> ")
        print num
        
        if num == '-1':
            print "Exiting"
            break
        elif not num.isdigit() or num == '0' or int(num) > 10:
            continue
        else:
            num = int(num)
            printoutput('DrWhoVillains.tsv', num)