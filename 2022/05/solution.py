with open("2022/05/input.txt", "r") as f:
    lines = f.readlines()

dock = {
    1: [x for x in 'DTRBJLWG'],
    2: [x for x in 'SWC'],
    3: [x for x in 'RZTM'],
    4: [x for x in 'DTCHSPV'],
    5: [x for x in 'GPTLDZ'],
    6: [x for x in 'FBRZJQCD'],
    7: [x for x in 'SBDJMFTR'],
    8: [x for x in 'LHRBTVM'],
    9: [x for x in 'QPDSV']
}

lines2 = [ line.strip().split(" ") for line in lines if "from" in line]
lines3 = [ [int(x[1]), int(x[3]), int(x[5])] for x in lines2 ]

def prettyprint(dock):
    for i in range(1, len(dock)+1):
        print(i, dock[i])

for instruction in lines3:
    count, source, dest = instruction
    
    blocks = dock[source][-count:]
    # toggle for parts 1 and 2
    # blocks.reverse()
    dock[source] = dock[source][:-count]
    dock[dest].extend(blocks)

result = "".join([dock[i][-1] for i in range(1, len(dock)+1)])
print(result)


