#!/user/bin/env/ python

for x in xrange(1, 101):
#	if x % 3 == 0 and x % 5 == 0:
	if x % 15 == 0:
		print "FizzBuzz"
	elif x % 3 == 0:
		print "Fizz"
	elif x % 5 == 0:
		print "Buzz"
	else:
		print x
