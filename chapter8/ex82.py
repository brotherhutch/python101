# ex 8.2 Python :: Mark Hutchison

#This one works -- print words[2] is now guarded by len(words) < 3
fhand = open('breakIt.txt')
count = 0
for line in fhand:
	words = line.split()
	# print 'Debug:', words
	if len(words) < 3 : continue
	if words[0] != 'From' : continue
	print words[2]

#This one breaks on the same file
fhand = open('breakIt.txt')
count = 0
for line in fhand:
	words = line.split()
	# print 'Debug:', words
	if len(words) == 0 : continue
	if words[0] != 'From' : continue
	print words[2]
	
