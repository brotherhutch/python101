# ex 5.2 Python :: Mark Hutchison
t = []
while True:
	try:
		num = raw_input('Enter a number: ')
		if num == "done" or num == "Done" :
			break
		num = float(num)
	except:
		print 'Invalid input'
		continue
	t.append(num)
print "Maximum: %g" % max(t)
print "Minimum: %g" % min(t)

