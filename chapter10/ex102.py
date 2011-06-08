# ex 10.2 Python :: Mark Hutchison
try:
	fname = raw_input('Enter filename: ')
	textfile = open(fname)
except:
	print 'You must enter a valid text filename'
	exit()
d = dict()
a = []
hlst = []
i = 0
for line in textfile:
	if line[:4] == "From" and not line[:5] == "From:" :
		words = line.split()
		a.append(words[5].split(':'))
for h, m, s in a :
	d[h] = d.get(h, 0) + 1
hlst = d.items()
hlst.sort()
while i < len(hlst) :
	print hlst[i][0], hlst[i][1]
	i = i + 1