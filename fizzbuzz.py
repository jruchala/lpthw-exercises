# FizzBuzz, a simple programming exercize based on the blog post
# http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/
# written by James Ruchala 11/19/2015

for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		print "fizzbuzz"
	elif i % 3 == 0:
		print "fizz"
	elif i % 5 == 0:
		print "buzz"
	else:
		print i