# ex 8.1 Python :: Mark Hutchison
def chop(t) :
	del t[0]
	del t[len(t)-1]

def middle(t) :
	return t[1:len(t)-1]

# test chop
lis = [1,2,3,4,5,6,7]
catch = chop (lis)

print lis
print catch

#test middle
oldlist = [9,8,7,6,5,4,3,2,1]
newlist =  middle(oldlist)

print newlist
print oldlist