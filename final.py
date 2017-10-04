import sys

myArray = []
inputVal = True
# Read the standard input
while inputVal == True:
	data = raw_input().strip()
	if data == "***":
	    inputVal = False
	    # break
	else
	    # d = data.split(" ")
	    myArray.append(data)
	    continue

nodes = myArray[0].split()
traversal = myArray[1]

del myArray[0:2]
print "Node Neighbors: "
# print myArray

# Node Neighbors
# newList = []
pin = []
for node in nodes:
	new = []
	new.append(node)
	for s in range(0, len(myArray)):
		arr = myArray[s].split(" ")
		if arr[0] == node:
			new.append(arr[1])
		elif arr[1] == node:
			new.append(arr[0])
	pin.append(new)
print pin

for n in range(len(pin)):
	ch = pin[n]
	ko = ' '.join(map(str, sorted(ch[1::])))
	print str(ch[0]) + ": " + ko
