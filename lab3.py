import sys
import math
from decimal import Decimal

# Read a file and check invaild file
if len(sys.argv) == 1:
	print "Don't forget to type your command line parameter"
	sys.exit()

# File reading with try/except
try:
	filename = sys.argv[1]
	file = open(filename).read().splitlines()
except:
	print "No!!!!!!Type correct file name."
	sys.exit()

# Create array for storing variables
array = []
# Create array for storing special variables
special = []

# Split the file by white space and store variables in the array
if ("ta" in filename):
	for apple in file:
		banana = apple.split(" ")
		for val in banana:
			# Split by '^'  
			v = val.split('^')
			for x in v:
				special.append(x)
	r = 1 
	s1 = float(special[1]) ** float(special[2])
	gn = float(special[6]) ** math.e
	c = Decimal(special[4])
	x = c
else:
	for apple in file:
		banana = apple.split(" ")
		for val in banana:
			array.append(val)
	r = 1			
	s1 = float(array[1])
	gn = float(array[5])
	c = float(array[3])
	x = c

# Initialize each variable
""" for example: 
s(1) = 4
c = 2
g(n) = 3
S(n) = 2S(n-1) + 3
"""
# g(n) == 0
if (gn == 0):
	# s(n) = p*x^n + q
	q = float(gn)/(1-c)
	p = (float(s1) - q)/ c

	sn = str(x) + "^" + "n"
	print "S(n) = " + sn

	# Calculate S(n)
	for n in range(1,11):
		s = p*c**n + q
		print "S" + "(" + str(n) + ") = " + str(s)

# Special case for TA FILE
elif (gn < 1):
	# s(n) = p*x^n + q
	q = Decimal(gn)/(1-c)
	p = (Decimal(s1)- Decimal(q))/ c

	sn = str(p) + " * " + str(x) + "^" + "n " + str(q)
	print "S(n) = " + sn

	# Calculate S(n)
	for n in range(1,11):
		s = p*c**n + q
		print "S" + "(" + str(n) + ") = " + str(s)
		
# Rest of it		
else:
	q = float(gn)/(1-c)
	p = (float(s1) - q)/ c

	sn = str(p) + " * " + str(x) + "^" + "n " + str(q)
	print "S(n) = " + sn

	# Calculate S(n)
	for n in range(1,11):
		s = p*c**n + q
		print "S" + "(" + str(n) + ") = " + str(s)		
