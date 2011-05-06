# ex 5.1 Python :: Mark Hutchison
total = 0
count = 0
average = 0
while True:
	try:
		num = raw_input('Enter a number: ')
		if num == "done" or num == "Done" :
			break
		num = float(num)
	except:
		print 'Invalid input'
		num = 0
		count = count - 1
	total = total + num
	count = count + 1
	average = total / count
print total, count, average
