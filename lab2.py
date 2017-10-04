import sys
import math

# sys.argv is a list in python, which contains the command-line arguments
# passed to the script & work with command line argument
# read a file
if len(sys.argv) == 1:
	print "Don't forget to type your command line parameter"
	sys.exit()

# file reading with try/except
try:
	filename = sys.argv[1]
	file = open(filename)
except:
	print "No!!!!!!!! Type correct file name."
	sys.exit()

# create array for storing variables
array = []

# split the file by white space and store variables in the array
for val in file:
	vals = val.split(" ")
	for v in vals:
		array.append(v)

# initialize each variable
s1 = int(array[1])
s2 = int(array[3])
c1 = int(array[5])
c2 = int(array[7])

# solution for quadratic equation
# (-b +/- -sqrt(b^2 - 4ac)) /2a 
r1 = ((c1) + math.sqrt((c1)**2 - (4*c2 * -1)))/2
r2 = ((c1) - math.sqrt((c1)**2 - (4*c2 * -1)))/2

if r1 == r2:
	# if r1 = r2 
	# p = S(1)
	# pr + qr = S(2)
	p = float(s1)
	q = s2/r1 - p
	# print output
	print "r1 = " + str(r1)
	print "r2 = " + str(r2)
	print "p = " + str(p)
	print "q = " + str(q)

	# S(n) =p*r^(n-1) + q*(n-1)*r^(n-1)
	sn = "(" + str(p) + ")" + "(" + str(r1) + ")" + "^" + "(n-1)" + " + " + "(" + str(q) + ")" + "(n-1)"+ "(" + str(r2) + ")" + "^(n-1)"
	print "S(n) = " + sn

	# calculate S(n)
	for n in range(1,11):
		s = p*r1**(n-1) + q*(n-1)*r2**(n-1)
		print "S("+str(n)+") = " + str(s)
else :
	# q = (s(2) - s(1)*r1)/(r2- r1)
	# p = s(1) - q
	q = (s2 - (s1*r1))/(r2 - r1)
	p = s1 - q

	# print output
	print "r1 = " + str(r1)
	print "r2 = " + str(r2)
	print "p = " + str(p)
	print "q = " + str(q)

	# s(n) = p*r^(n-1) + q*(n-1)^(n-1)
	sn = "(" + str(p) + ")" + "(" + str(r1) + ")" + "^" + "(n-1)" + " + " + "(" + str(q) + ")" + "(" + str(r2) + ")" + "^(n-1)"
	print "S(n) = " + sn

	# calculate S(n)
	for n in range(1,11):
		s = p*r1**(n-1) + q*r2**(n-1)
		print "S(" + str(n) + ") = " + str(s)


