# ex 3.2 Python :: Mark Hutchison
try:
	hrs = float(raw_input('Enter hours: '))
	rate = float(raw_input('Enter rate: '))
except:
	print 'Oops! I need a number.'
	exit()
if hrs > 40.0 :
	basepay = 40.0 * rate
	OThrs = hrs - 40.0
	OTrate = rate * 1.5
	OTpay = OTrate * OThrs
	pay = basepay + OTpay
else :
	pay = hrs * rate
print 'Your pay: ' + str(round(pay,2))
