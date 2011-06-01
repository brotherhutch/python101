# ex 8.3 Python :: Mark Hutchison
try:
	fname = raw_input('Enter filename: ')
	tf = open(fname)
except:
	print 'You must enter a valid text filename'
	exit()
t = []
for li in tf:
	words = li.split()
	for word in words:
		if word in t: continue
		t.append(word)
t.sort()
print t