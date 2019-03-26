""" This simple module provides functions to be used for part 1 and
    part 2 of the homework. Each function is described in detail below.

To use this module, import it first::
 
    import hw4_util

"""


def read_games(filename):
    """This function is to be used for part1 of the homework.

    Reads a file containing all the games in the 2014 World Cup Soccer.
    It returns a list of lists.
    
    Call this function as:

    results = hw4_util.read_games(filename)

    For example, if you are given the following file contents:

    Brazil,3,Croatia,1,Brazil
    Netherlands,0,Costa Rica,0,Netherlands

    The above call will return the following list:

    [['Brazil', 3, 'Croatia', 1, 'Brazil'],\
     ['Netherlands', 0, 'Costa Rica', 0, 'Netherlands']]
    
    """

    results = []
    for line in open(filename):
        m = line.strip().split(",")
        m[1] = int(m[1])
        m[3] = int(m[3])
        results.append(m)
    return results


def read_medals(filename):
    """This function is to be used for part3 of the homework.

    Reads a file containing medals for different countries. 
    It returns a list of lists.
    
    Call this function as:

    medals = hw4_util.read_medals(filename)

    For example, if you are given the following file contents:

    1, United States, 9, 15, 13, 37
    2, Germany, 10, 13, 7, 30

    The above call will return the following list:

    [['United States', 9, 15, 13, 37], ['Germany', 10, 13, 7, 30]]
    
    """

    medals = []
    for line in open(filename):
        line = line.strip("\n")
        items = line.split(",")
        items[1] = items[1].strip()
        for i in range(2, len(items)):
            items[i] = int(items[i])
        medals.append(items[1:])
    return medals


