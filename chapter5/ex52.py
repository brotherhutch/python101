# ex 5.2 Python :: Mark Hutchison
minN = None
maxN = None
while True:
	try:
		num = raw_input('Enter a number: ')
		if num == "done" or num == "Done" :
			break
		num = float(num)
	except:
		print 'Invalid input'
		continue
	if maxN == None or maxN < num :
		maxN = num
	if minN == None or num < minN :
		minN = num
print minN, maxN
