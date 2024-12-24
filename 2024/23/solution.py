from collections import defaultdict

debugFile = ''
board= list()

nodes = defaultdict(set)

with open("./input."+debugFile+".txt" if debugFile else "./input.txt", "r") as f:
  for line in f.readlines():
    left, right = line.strip().split('-')

    nodes[left].add(right)
    nodes[right].add(left)


# set of sorted 3 node items where items start with t
triSets=set()

for nodeA in nodes.keys():
  for nodeB in nodes[nodeA]:
    for nodeC in nodes.keys():
      if nodeC == nodeA or nodeC == nodeB: continue

      if nodeC in nodes[nodeA] and nodeC in nodes[nodeB]:
        sortedTriset = tuple(sorted((nodeA, nodeB, nodeC)))
        triSets.add(sortedTriset)

            # A - B
            # \  /
            #  C  

justTs = set()
for triSet in triSets:
  for c in triSet:
    if c.startswith('t'):
      justTs.add(triSet)
print(len(justTs))


searching = True
xSets = defaultdict(set)
xSets[3] =triSets 

# this isn't the most efficient way to find this but adding things one by one does get there eventually :)
while searching:
  searching = False
  largestVal = max(xSets.keys())

  for xSet in xSets[largestVal]:
    for node in nodes.keys():
      if node in xSet: continue

      # if node is connected to all values create an largestVal+1 set
      if all(x in nodes[node] for x in xSet):
        searching = True
        newXSet = list(xSet)
        newXSet.append(node)
        newXSet = tuple(sorted(newXSet))

        xSets[largestVal+1].add(newXSet)

  if searching:
    # print(xSets[largestVal+1])
    print(f"found {len(xSets[largestVal+1])} sets with {largestVal+1} nodes")
      


largestVal = max(xSets.keys())
if len(xSets[largestVal]) != 1: print('somethings wrong')
answer = ','.join(xSets[largestVal].pop())
print(answer)




