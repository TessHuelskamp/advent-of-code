from copy import copy 

lines=list()
with open("./input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

allgroups = list()
curgroup = set()
for line in lines:
    if len(line) == 0:
        allgroups.append(copy(curgroup))
        curgroup = set()
    else:
        for c in line:
            curgroup.add(c)
allgroups.append(copy(curgroup))

print(sum(len(g) for g in allgroups))


allgroups = list()
curgroup = dict()
groupSize=0
for line in lines:
    if len(line) == 0:
        curgroup["size"]=groupSize
        allgroups.append(copy(curgroup))
        curgroup = dict()
        groupSize=0
    else:
        groupSize+=1
        for c in line:
            if c not in curgroup:
                curgroup[c]=0
            curgroup[c]+=1

curgroup["size"]=groupSize
allgroups.append(copy(curgroup))

def numAnswers(group):
    groupSize = group["size"]
    numAnswers=0

    for key, value in group.items():
        if key == "size": continue
        if value == groupSize:
            numAnswers+=1

    return numAnswers

print(sum(numAnswers(g) for g in allgroups))
