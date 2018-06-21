def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

# 1st call - (2.0+3.0) /(2.0 - 3.0)= 5.0/ -1.0 = -5
# 2nd call  - (3.0 + 3.0)/ (3.0 -3.0) = 6.0/ 0 = ZeroDivisionError    which handeled so
# output   : -5.0
# output :   a/b result in 0