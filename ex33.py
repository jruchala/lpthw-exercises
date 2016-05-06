# i = 0
# numbers = []

# while i < 6:
	# print "At the top i is %d" % i
	# numbers.append(i)
	
	# i += 1
	# print "Numbers now: ", numbers
	# print "At the bottom i is %d" % i
	
# print "The numbers: "

# for num in numbers:
	# print num
	
# def a_for_loop(maximum):
	# i = 0
	# numbers = []
	# while i < maximum:
		# print "At the top i is %d" % i
		# numbers.append(i)
		
		# i += 1
		# print "Numbers now: ", numbers
		# print "At the bottom i is %d" % i
	
	# print "The numbers: "
	# for num in numbers:
		# print num
	
	
	# print num
	
# def a_for_loop(maximum, incrementi):
	# i = 0
	# numbers = []
	# while i < maximum:
		# print "At the top i is %d" % i
		# numbers.append(i)
		
		# i = i + incrementi
		# print "Numbers now: ", numbers
		# print "At the bottom i is %d" % i
	
	# print "The numbers: "
	# for num in numbers:
		# print num

def a_for_loop(maximum, incrementi):
	i = 0
	numbers = []
	for i in range(0, maximum):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "
	for num in numbers:
		print num
		
a_for_loop(6, 2)
