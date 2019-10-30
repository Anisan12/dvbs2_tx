f = open("dvbs2.conf", "r")
lines = f.readlines()
for i in range(0, len(lines)):
	value = lines[i]
	value = int(value)
	print(value)
f.close()
