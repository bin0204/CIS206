# read data
data = raw_input().strip()
x = data.split(" ")
y = 2**(len(x)-1)

# arrays
first = []
second = []
count = 0
garb = raw_input()
while count < y:
    z = raw_input().strip()
    if z == "":
        break
    z1 = z.split(" ")
    if z1[-1] == "1":
         first.append(z1)
    elif z1[-1] == "0":
        second.append(z1)
    count += 1

output = []

# when out is 1
for a in first:
    for b in range(0,len(a)-1):
        if a[b] == "1":
            a[b] = x[b]
        elif a[b] == "0":
            a[b] = x[b] + "'"
    output.append(" ".join(a[:-1]))
print "DNF: " + " + ".join(output)

output = []
for a in second:
    for b in range(0,len(a)-1):
        if a[b] == "1":
            a[b] = x[b] + "'"
        elif a[b] == "0":
            a[b] = x[b]
    output.append("("+ " + ".join(a[:-1])+ ")")
print "CNF: " + "".join(output)
