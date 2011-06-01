# ex 8.3 Python :: Mark Hutchison
try:
	fname = raw_input('Enter filename: ')
	textfile = open(fname)
except:
	print 'You must enter a valid text filename'
	exit()
count = 0
for line in textfile:
	if line[:4] == "From" and not line[:5] == "From:" :
		words = line.split()
		print words[1]
		count = count + 1
print "There were %d lines in the file with From as the first word." % count