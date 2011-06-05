# ex 9.4 Python :: Mark Hutchison
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
		a.append(words[1])
for address in a :
	d[address] = d.get(address, 0) + 1
mx = None
for item in d :
	if mx == None or mx < d[item] :
		mx = d[item]
		result = str(item) + ' ' + str(d[item])
print result
