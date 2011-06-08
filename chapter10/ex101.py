# ex 10.1 Python :: Mark Hutchison
try:
	fname = raw_input('Enter filename: ')
	textfile = open(fname)
except:
	print 'You must enter a valid text filename'
	exit()
t = ()
d = {}
a = []
tlst = []
for line in textfile:
	if line[:4] == "From" and not line[:5] == "From:" :
		words = line.split()
		a.append(words[1])
for address in a :
	d[address] = d.get(address, 0) + 1
for email, count in d.items() :
	tlst.append((count, email))
tlst.sort(reverse=True)
print tlst[0][1], tlst[0][0]