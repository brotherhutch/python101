# ex 9.3 Python :: Mark Hutchison
try:
	fname = raw_input('Enter filename: ')
	textfile = open(fname)
except:
	print 'You must enter a valid text filename'
	exit()
count = 0
d = dict()
a = []
for line in textfile:
	if line[:4] == "From" and not line[:5] == "From:" :
		words = line.split()
		a.append(words[2])
for day in a :
	d[day] = d.get(day, 0) + 1
print d
