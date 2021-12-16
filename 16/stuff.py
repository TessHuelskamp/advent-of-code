import itertools
with open("./input.txt", "r") as f:
    chars = list(f.readline().strip())

bits = map(lambda x: bin(int(x, 16)), chars)
bitsLeadingZeros = map(lambda x: x[2:].zfill(4), bits)
allBits = "".join(bitsLeadingZeros)

packetIndex=0
sumVersionNumbers = 0

packets = dict()
def parse(packetIndex):
    global sumVersionNumbers
    while packetIndex < len(allBits):
        ogStart=packetIndex
        packetString=""

        # Ignore the trailing zeros
        stuff = allBits.find("1", packetIndex)
        if stuff < 0:
            break

        version = allBits[packetIndex:packetIndex+3]
        typeID = allBits[packetIndex+3:packetIndex+6]
        versionInt = int(version, 2)
        typeIDInt = int(typeID, 2)

        packetString = "l:" if typeIDInt == 4 else "x:"
        packetString += version + "," + typeID

        packetIndex += 6
        sumVersionNumbers += versionInt


        if typeIDInt == 4:
            # Literal value.
            # Single binary number broken into groups of 4.
            # It's split into chunks of 5. If the first bit is 1 we should continue else this is the last chunk
            literalBits = ""
            shouldContinue=True
            while shouldContinue:
                shouldContinue = allBits[packetIndex] == "1"
                literalBits += allBits[packetIndex+1:packetIndex+5]
                packetString += allBits[packetIndex:packetIndex+5]
                packetIndex += 5
                if shouldContinue:
                    packetString+= ","
            literal = int(literalBits, 2)
        else:
            lengthTypeBit = allBits[packetIndex]
            packetString += lengthTypeBit + ","
            packetIndex += 1
            if lengthTypeBit == "0":
                # 15 bits describe length of subpacket
                packetIndex += 15
                packetString+= allBits[packetIndex:packetIndex+15]
            elif lengthTypeBit == "1":
                packetIndex += 11
                packetString+= allBits[packetIndex:packetIndex+11]


        packets[ogStart] = packetString
        packetSize = packetIndex-ogStart
        assert packetSize == sum(1 for x in packetString if x in "01")
        print(ogStart, packetIndex-ogStart, packetString)
    
parse(0)
assert sumVersionNumbers == 951
print(sumVersionNumbers)

