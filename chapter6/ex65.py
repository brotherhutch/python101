# ex 6.5 Python :: Mark Hutchison
str = 'X-DSPAM-Confidence: 0.8475'
startpos = str.find(':')
newNUM = float( str[startpos+1:].strip() )
print newNUM