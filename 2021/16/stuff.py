import itertools
with open("./input.txt", "r") as f:
    chars = list(f.readline().strip())

bits = map(lambda x: bin(int(x, 16)), chars)
bitsLeadingZeros = map(lambda x: x[2:].zfill(4), bits)
allBits = "".join(bitsLeadingZeros)

packetIndex=0
sumVersionNumbers = 0

#start index and string
packets = dict()
def originalParse(packetIndex):
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
                packetString+= allBits[packetIndex:packetIndex+15]
                packetIndex += 15
            elif lengthTypeBit == "1":
                packetString+= allBits[packetIndex:packetIndex+11]
                packetIndex += 11


        packets[ogStart] = packetString
        packetSize = packetIndex-ogStart
        assert packetSize == sum(1 for x in packetString if x in "01")

sumVersion2= 0
def parse2(packetIndex):
    if packetIndex not in packets:
        raise Exception("Somethings wrong")
    global sumVersion2

    ogStart=packetIndex
    packetString=""

    version = allBits[packetIndex:packetIndex+3]
    typeID = allBits[packetIndex+3:packetIndex+6]
    versionInt = int(version, 2)
    typeIDInt = int(typeID, 2)

    sumVersion2 += versionInt

    packetString = "l:" if typeIDInt == 4 else "x:"
    packetString += version + "," + typeID

    packetIndex += 6

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
        return literal, packetIndex-ogStart

    lengthTypeBit = allBits[packetIndex]
    packetString += lengthTypeBit + ","
    packetIndex += 1

    isBitCount = lengthTypeBit == "0"
    childrenValues=list()
    childrenSize=0
    if isBitCount:
        # 15 bits describe length of subpacket
        lengthBits = allBits[packetIndex:packetIndex+15]
        packetIndex += 15
        packetString += lengthBits
        subPacketBits = int(lengthBits, 2)

        while subPacketBits - childrenSize > 0:
            value, size = parse2(packetIndex+childrenSize)
            childrenValues.append(value)
            childrenSize += size
    else:
        lengthBits = allBits[packetIndex:packetIndex+11]
        packetString += lengthBits
        numSubPackets = int(lengthBits, 2)
        packetIndex += 11
        for _ in range(numSubPackets):
            value, size = parse2(packetIndex+childrenSize)
            childrenValues.append(value)
            childrenSize += size

    packetSize = packetIndex - ogStart
    totalSize = packetSize + childrenSize

    strByOpCode={0:"sum", 1:"prod", 2:"min", 3:"max", 5:"gt", 6:"lt", 7:"eq"}
    #print(strByOpCode[typeIDInt], childrenValues)

    if typeIDInt == 0:
        return sum(childrenValues), totalSize
    elif typeIDInt == 1:
        res = 1
        for val in childrenValues:
            res *= val
        return res, totalSize
    elif typeIDInt == 2:
        return min(childrenValues), totalSize
    elif typeIDInt == 3:
        return max(childrenValues), totalSize
    elif typeIDInt == 5:
        assert len(childrenValues) == 2
        res = 1 if childrenValues[0] > childrenValues[1] else 0
        return res, totalSize
    elif typeIDInt == 6:
        assert len(childrenValues) == 2
        res = 1 if childrenValues[0] < childrenValues[1] else 0
        return res, totalSize
    elif typeIDInt == 7:
        assert len(childrenValues) == 2
        res = 1 if childrenValues[0] == childrenValues[1] else 0
        return res, totalSize


originalParse(0)
assert sumVersionNumbers == 951
print(sumVersionNumbers)

response, size = parse2(0)

assert sumVersion2==sumVersionNumbers
assert response < 939000762979
print(response)
