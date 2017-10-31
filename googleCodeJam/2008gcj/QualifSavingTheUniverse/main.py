
SortedData = []
tempList = []

with open("A-small-practice.in") as fp:
    for i, line in enumerate(fp):
        line = line.rstrip() #remove \n
        if i == 0:
            caseNumber = line
        else:
            if not line.isdigit(): # if a string, store into a temporary list
                tempList.append((line))
            if line.isdigit() and i != 1 : # if a number, store the temporary list into the SortedData and RAZ tempList
                SortedData.append(tempList)
                tempList = []
SortedData.append(tempList) # to save the last list

print SortedData.__len__()


# listSearchEngines = SortedData[0]
# listQueries = SortedData[1]
# if listQueries.__len__() == 0:
#     print "Case #", 1, ":", 0

listSearchEngines = SortedData[2]
listQueries = SortedData[3]

# comparer les 2 listes, s il n y en a pas en commun, choisir celui la


