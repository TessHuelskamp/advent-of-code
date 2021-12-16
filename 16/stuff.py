import itertools
with open("./input.txt", "r") as f:
    chars = list(f.readline().strip())

bits = map(lambda x: bin(int(x, 16)), chars)
bitsLeadingZeros = map(lambda x: x[2:].zfill(4), bits)


allBits = "".join(bitsLeadingZeros)

packetStart=0
sumVersionNumbers = 0
try:
    while packetStart < len(allBits):
        version = allBits[packetStart:packetStart+3]
        typeID = allBits[packetStart+3:packetStart+6]
        versionInt = int(version, 2)
        typeIDInt = int(typeID, 2)

        if typeIDInt == 4:
            print("literal")
        else:
            print("not literal")

        print(allBits[packetStart:packetStart+3], end=",")
        print(allBits[packetStart+3:packetStart+6], end=",")

        packetStart += 6 
        sumVersionNumbers += versionInt


        if typeIDInt == 4:
            # Literal value.
            # Single binary number broken into groups of 4.
            # It's split into chunks of 5. If the first bit is 1 we should continue else this is the last chunk
            literalBits = ""
            shouldContinue=True
            while shouldContinue:
                shouldContinue = allBits[packetStart] == "1"
                literalBits += allBits[packetStart+1:packetStart+5]
                print(allBits[packetStart:packetStart+5], end=",")
                packetStart += 5
            literal = int(literalBits, 2)

        else:
            lengthTypeBit = allBits[packetStart]
            print(lengthTypeBit, end=",")
            packetStart += 1 
            if lengthTypeBit == "0":
                # 15 bits describe length of subpacket
                packetStart += 15
                print(allBits[packetStart:packetStart+15], end=",")
                # TODO sub processing
            elif lengthTypeBit == "1":
                packetStart += 11
                print(allBits[packetStart:packetStart+11], end=",")
                # contains number of subpackets that are part of this packet
        print()
except IndexError:
    # trailing zeros are fine I guess :sweat:
    print()
    print(packetStart)
    pass

assert sumVersionNumbers == 951
print(sumVersionNumbers)

