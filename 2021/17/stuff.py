#target area: x=179..201, y=-109..-63
xStart, xEnd = 179, 201
yStart, yEnd = -63, -109


def runShot(vx, vy):
    posX, posY = 0, 0
    maxY=0

    while posX <= xEnd and posY > yEnd:
        posX+=vx
        posY+=vy

        #print(x, y, vx, vy)

        maxY = max(maxY, posY)

        if abs(vx) > 0:
            delta = -1 if vx > 0 else 1
            vx += delta
        vy -=1

        hitTarget = xStart <= posX <= xEnd and yEnd <= posY <= yStart
        if hitTarget:
            return True, maxY

        #print(yEnd, posY, posY < yEnd)

    # TODO, too short or too long???
    return False, None



results = list()
countSuccess = 0
# Brute force. Nothign special here :)
# X has to be positive to work :)
for x in range(1, xEnd+1):
    # Y can be negative
    for y in range(-200, 1000):
        success, yMax = runShot(x, y)
        if success:
            results.append(yMax)
            countSuccess+=1

maxY = max(results)
print(maxY)
assert maxY == 5886
print(countSuccess)
assert countSuccess == 1806
