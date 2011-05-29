# ex 4.4 Python :: Mark Hutchison
def computepay(h, r):
	try:
		hrs = float(h)
		rate = float(r)
	except:
		print 'Oops! I need a number.'
		return
	if hrs > 40.0 :
		basepay = 40.0 * rate
		OThrs = hrs - 40.0
		OTrate = rate * 1.5
		OTpay = OTrate * OThrs
		pay = basepay + OTpay
	else :
		pay = hrs * rate
	print 'Hours: ' + str(hrs)
	print 'Rate: ' + str(rate)
	print 'Your pay: ' + str(round(pay,2))

computepay(18, 19)
computepay(8.5, 10.25)
computepay('frog', 'toad')
computepay(50, 10)

