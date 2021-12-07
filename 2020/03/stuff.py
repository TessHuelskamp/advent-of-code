
lines=list()
with open("./input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

treeSize=len(lines[0])

def numCollisions(right, down):
    index=0
    numTrees=0

    for i, line in enumerate(lines):

        if down == 2 and i%2==1:
            continue

        if line[index]=="#":
            numTrees+=1

        index+=right
        index%=treeSize

    return numTrees

totalProduct=1
for right in [1, 3, 5, 7]:
    coll = numCollisions(right, 1)
    print(right, coll)
    totalProduct *= coll

coll = numCollisions(1, 2)
totalProduct *= coll

print(totalProduct)


