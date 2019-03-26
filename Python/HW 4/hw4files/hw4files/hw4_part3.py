
"""


This code takes as input a string and a line length, and then prints that string, stopping it after it reaches the line length and then moves it onto the next line for 10 lines.

"""
string = raw_input("Please enter a line ==> ")
print string

length = int(raw_input("Please enter a line length ==> "))
print length

string = (string + " ") * (length)

i = 0

while i < 10:
    if (string[0] == " "):
        print "%s"%(string[1:length])
    else:
        print "%s"%(string[:length])
    string = string[length:]
    i += 1 