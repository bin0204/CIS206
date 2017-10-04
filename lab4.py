# read the input 
inputs = 0
count = 0.0
array = []
do = []
co = []
rel = []
evenRel = []
oddRel = []
comRel = []

# split the file by white space and store variables into different array
while count < 3:
	y = raw_input().strip()
	vals = y.split(" ")
	array.append(vals)
	count += 1

# Domain
for a in array[0]:
	do.append(a)
print do

# Codomain
for b in array[1]:
	co.append(b)
print co

# Relation
for c in array[2]:
	rel.append(c)
print rel

# Put all the even elements into evenRel
# Elements from list1 starting from 0 iterating by 2
evenRel = rel[::2]
# rel%2 == 0 
print evenRel

# Put all the odd elements into evenRel
# Elements from list1 starting from 1 iterating by 2
oddRel = rel[1::2]
print oddRel
# combine odd and even relation
for v in range(len(oddRel)):
	rel = "(" + oddRel[v] + ", " + evenRel[v] + ")"
	comRel.append(rel)
	v += 1
print comRel	

# Print outputs
domain = ", ".join(do)
codomain = ", ".join(co)
relation = ", ".join(comRel)

print "DOMAIN: { " + domain + " }"
print "CODOMAIN: { " + codomain + " }"
print "RELATION: { " + relation + " }"

# sort to compare each elements
oddRel.sort()
evenRel.sort() 
# domain
do.sort() 

# whether function is or not
if (evenRel == do):
	print "This is a function"
	# whether function is onto or not
	if (set(oddRel) == set(co)):
		print "It is onto"	
		# check if the codomain is used more than one time
		if (len(set(oddRel)) == len(do)):
			print "It is one-to-one."
			print "It is a bijection"
		else:
			print "It is *not* one-to-one."			
			print "It is *not* a bijection"	
	else:
		print "It is *not* onto"					
else:
	print "This is *not* a function"

