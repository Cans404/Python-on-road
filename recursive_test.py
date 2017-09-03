#!/bin/python

least = 1

def get_peach(n):
	if n == 5:
		return least
	else:
		if (get_peach(n+1)*5+1)%4 == 0:
			return (get_peach(n+1)*5+1)/4
		else:
			return -1

while True:
	num = get_peach(1)
	if num == -1:
		least += 1
	else:
		break

print "there are at least %d peachs at first." % (num*5+1)
print "in case of this, first monkey get %d peachs." % num
