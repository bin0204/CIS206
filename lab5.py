count = 0
array = []

# First line contains a message in plain text
# Second line will be numeric value k that specifies
# the key to be used to encode the message

# Read the standard input 
while count < 2:
	x = raw_input().strip()
	array.append(x)
	count += 1
print array	

# Make arrays for message and key
message = array[0]
# Type was string, so required to convert from string to integer for calculating
key = int(array[1])

print type(key)
print message
print key

# Store the encoded message into encode array
encode = []

# ord() function: built in function and given a string representing one Unicode character
# Return an integer representing the Unicode code point of that character
# For instance, ord('A') returns the integer 65 number that represents letter in ASCII
for i in message:
	# Spaces 
	if (i == " "):
		# spaces in the text
		encode.append(i)
	else:
		# f(x) = (g(p) + key)mod 26
		# Type is integer
	 	x = (ord(i) - 65 + key) % 26
	 	# Use chr() function to convert from integer to character 
	 	# Add 65 for generating ASCII code
	 	encode.append(chr(x+65))	

# Do not need any marks or characters between code, so just join ""
print "".join(encode)
