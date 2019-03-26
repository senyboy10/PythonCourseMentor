"""

Author: ALSENY SYLLA

This code takes as input the paths of two people, and lists their location at every point in the path, as well as the distance between the two people at every point. It also lists the minimum and maximum distance after all distances have been displayed.

"""
def location(par, loc): #function changes location based on whether person moved up, down, left, right
    if par == 'up':
        loc[1] += 1
    elif par == 'down':
        loc[1] -= 1
    elif par == 'left':
        loc[0] -= 1
    elif par == 'right':
        loc[0] += 1

    
path1 = raw_input("Enter the first path ==> ")
print path1
path1 = path1.split(",")

loc1 = []
loc1.append(int(path1[1]))
loc1.append(int(path1[2]))

path2 = raw_input("Enter the second path ==> ")
print path2
path2 = path2.split(",")

loc2 = []
loc2.append(int(path2[1]))
loc2.append(int(path2[2]))

print path1[0].ljust(11) + "Action".ljust(11) + path2[0].ljust(11) + "Action".ljust(11) + "Distance".ljust(11)
d = (int(path2[1])-int(path1[1])) + (int(path2[2])-int(path1[2]))
print str(tuple(loc1)).ljust(11) + "initial".ljust(11) + str(tuple(loc2)).ljust(11) + "initial".ljust(11) + str((int(path2[1])-int(path1[1]))+(int(path2[2])-int(path1[2]))).ljust(11)

lists1 = []
for i in range (3, len(path1)):
    location(path1[i], loc1)
    lists1.append(tuple(loc1))
    
lists2 = []
for j in range (3, len(path2)):
    location(path2[j], loc2)
    lists2.append(tuple(loc2))

dist = [d]
for k in range(0, len(lists1)):
    x1 = int(lists1[k][0])
    y1 = int(lists1[k][1])
    x2 = int(lists2[k][0])
    y2 = int(lists2[k][1])
    distance = abs(x2 - x1) + abs(y2 - y1)
    dist.append(distance)
    print str(lists1[k]).ljust(11) + path1[k+3].ljust(11) + str(lists2[k]).ljust(11) + path2[k+3].ljust(11) + str(distance)
    
print "The minimum distance between them is " + str(min(dist))
print "The maximum distance between them is " + str(max(dist))