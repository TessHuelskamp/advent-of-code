lines=list()
with open("./input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

# graph problem

# {color : { color: num}}
graph = dict()

def getName(left, right): return left+"-"+right

for rule in lines:
    rule = rule[:-1]
    words = rule.split(" ")

    color = getName(words[0], words[1])
    graph[color]=dict()

    if "no other bags" in rule:
        continue

    bags = words[4:]
    assert len(bags) %4 ==0
    numBags = len(bags)/4

    for i in range(numBags):
        base=4*i
        num = int(bags[base])
        subcolor = getName(bags[base+1], bags[base+2])
        graph[color][subcolor]=num

shinygold="shiny-gold"
weKnowYes=set()
weKnowNo=set()
def cancontain(color):
    if color in weKnowYes:
        return True
    elif color in weKnowNo:
        return False

    thing = graph[color]
    if shinygold in thing:
        weKnowYes.add(color)
        return True
    for node in thing.keys():
        result = cancontain(node)
        if result:
            weKnowYes.add(color)
            return True
    weKnowNo.add(color)
    return False


num=0
for color in graph.keys():
    if cancontain(color):
        num+=1
print(num)

def getTotal(color):
    total = 0

    node = graph[color]
    for nodeColor, num in node.items():
        total += num * (getTotal(nodeColor)+1)
    return total

print(getTotal(shinygold))

