# ex 3.1 Python :: Mark Hutchison
hrs = raw_input('Enter hours: ')
rate = raw_input('Enter rate: ')
if float(hrs) > 40.0 :
	basepay = 40.0 * float(rate)
	OThrs = float(hrs) - 40.0;
	OTrate = float(rate) * 1.5
	OTpay = float(OTrate) * float(OThrs)
	pay = basepay + OTpay
else :
	pay = float(hrs) * float(rate)
print 'Your pay: ' + str(round(pay,2))