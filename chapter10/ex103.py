# -*- coding: utf-8 -*-
# ex 10.3 Python :: Mark Hutchison
import string

def most_frequent (s) :
	i = 0
	ls1 = []
	ls2 = []
	d = {}
	s = s.translate(None, string.punctuation)
	s = s.translate(None, ' ')
	s = s.lower()
	while i < len(s) :
		ls1.append(s[i])
		i = i + 1
	for lr in ls1 :
		d[lr] = d.get(lr,0) + 1
	for key, value in d.items() :
		ls2.append( (value, key) )
	ls2.sort(reverse=True)
	for srtlr in ls2 :
		print srtlr[0] , srtlr[1]
print 'English'
most_frequent('The frequency of letters in text has often been studied for use in cryptography, and frequency analysis in particular. No exact letter frequency distribution underlies a given language, since all writers write slightly differently.')

print 'Deutsch'
most_frequent('Schweden ist eines der größten Länder Europas und weist im Hinblick auf die Natur und das Klima beträchtliche regionale Unterschiede auf. Die unverwechselbare blau-gelbe Flagge ist eines der nationalen Wahrzeichen, die die jahrhundertelange Geschichte und Beziehung des Landes mit seinen nordischen Nachbarn widerspiegeln')

print 'French'
most_frequent('Les titulaires d’un visa d’entrée et de long séjour portant la mention « Carte de séjour à solliciter à l’arrivée en France » doivent prendre contact avec l’autorité préfectorale française afin de déposer une demande de carte de séjour dans les deux mois après leur entrée sur le territoire français.')