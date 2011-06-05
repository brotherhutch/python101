# ex 9.5 Python :: Mark Hutchison
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
		domain = words[1][words[1].find('@')+1:]
		a.append(domain)
for address in a :
	d[address] = d.get(address, 0) + 1
print d