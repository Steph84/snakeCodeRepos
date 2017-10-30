# A-small-practice.in

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Code Jam problems.
f = open('A-small-practice.in', 'r')
caseNumber = (int)f.readline()

for i in xrange(1, caseNumber + 1):
    queriesNumber = int(raw_input())
    for j in xrange(1, queriesNumber + 1):
        query = raw_input()  # read a list of integers, 2 in this case
        print "Case #{}: query #{} {}".format(i, j, query)
# check out .format's specification for more formatting options
