string = input("Please Enter a line ==> ")
print(string)
length = int(input("please enter a line length ==> "))
print(length)

string = (string + " ") * (length)
print(string)

i = 0
while(i < 10):
	if(string[0] == " "):
		print (string[1:length])
	else:
		print (string[:length])
	string = string[:length]
	i += 1 