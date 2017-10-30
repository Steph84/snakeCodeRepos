# A-small-practice.in

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Code Jam problems.

myList = []
yoshi = []

with open("A-small-practice.in") as fp:
    for i, line in enumerate(fp):
        myList.append((line))
        if line.isdigit():
            print "fuck"

print myList.__len__()
caseNumber = int(myList[0])
print caseNumber
for x in myList:
    x.split('\n')
    if x.isdigit():
        print x

#caseNumber = int(line)
#pass
#queriesNumber = int(line)
#for j in range(i, i+queriesNumber):
#    print line





