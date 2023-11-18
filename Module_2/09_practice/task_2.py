zen = open("zen.txt", "r")
zen_lines = zen.readlines()
zen.close()
for line in zen_lines[::-1]:
	print(line, end="")
