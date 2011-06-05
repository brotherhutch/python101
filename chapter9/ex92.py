# ex 9.2 Python :: Mark Hutchison
def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c,0) + 1
	return d

h = histogram('brontosaurus')
print h