# ex 8.3 Python :: Mark Hutchison
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
	words = line.split()
	# print 'Debug:', words
	if len(words) >= 3 and words[0] == 'From' : print words[2]