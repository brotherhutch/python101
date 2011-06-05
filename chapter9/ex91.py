# ex 9.1 Python :: Mark Hutchison
tfile = open('words.txt')
i=0
lst = {}
for line in tfile:
	words = line.split()
	for word in words:
		lst[word] = i
		i=i+1
print 'magna' in lst