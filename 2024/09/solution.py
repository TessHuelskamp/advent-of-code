debugFileName = ""

debug = bool(debugFileName)

# crimes against characters here but all of the files are the size of one char :)
ZERO_CHAR = "0"
def toChar(fileNum):
  return chr(ord(ZERO_CHAR)+fileNum)

def toFileNum(char):
  return ord(char) - ord(ZERO_CHAR)

def expandCompactBlock():
  disk = ""
  for i, val in enumerate(compactBlock):
    if i%2==0: # even is a file
      fileNum = int(i/2)
      disk += toChar(fileNum)*int(val)
    else:
      # odd is free space
      disk += "."*int(val)
  
  return disk.strip(".")

def getCheckSum(diskList):
  checkSum = 0
  for i, val in enumerate(diskList):
    if val == ".": continue

    fileNum = toFileNum(val)
    checkSum += fileNum * i

  return checkSum

with open("./input."+debugFileName+".txt" if debugFileName else "./input.txt", "r") as f:
  compactBlock = f.readline().strip()

  # print(compactBlock)



# Part 1
disk = expandCompactBlock()

diskList = list(disk)
while "." in diskList:

  # find the first "." and move the last char over it
  # delete the last char and then lop off any remaining dots that are now free
  idx = diskList.index(".")
  diskList[idx]=diskList[-1]
  diskList[-1]="."

  while diskList[-1] == ".":
    del diskList[-1]

print(getCheckSum(diskList))


# Part 2 

def findSizeOfBlock(char, startIdx):
  if diskList[startIdx] != char:
    raise Exception("invalid input go away")
  
  length = 1
  nextSpot = startIdx+length
  
  while nextSpot < len(diskList) and diskList[nextSpot] == char:
    length +=1
    nextSpot = startIdx+length
  
  return length
  

def findFreeSpace(neededSize, end):
  start=0
  
  while start < end:
    firstIdx = diskList.index(".", start)
    
    # happens when filesystem is contiguous
    # We dont want files to jump to the right :)
    if firstIdx and end <= firstIdx:
      return None
    
    blockSize = findSizeOfBlock(".", firstIdx)

    if neededSize <= blockSize:
      return firstIdx
    
    start=firstIdx+blockSize
  
  return None



diskList = list(expandCompactBlock())
currentChar = diskList[-1]


if debug: print ("".join(diskList))
while currentChar != ZERO_CHAR:
  # Find the first spot where the char exists and figure out its length
  fileStartIdx = diskList.index(currentChar)
  size = findSizeOfBlock(currentChar, fileStartIdx)
  
  freeSpaceIdx = findFreeSpace(size, fileStartIdx)

  if freeSpaceIdx:
    # free up old space
    for i in range(size): diskList[fileStartIdx+i] = "."
    for i in range(size): diskList[freeSpaceIdx+i] = currentChar
      
  
  # move on to the next char
  currentChar = toChar(toFileNum(currentChar)-1)

  if debug: print("".join(diskList))

  currentCharIdx = toFileNum(currentChar)
  # if currentCharIdx%1000 == 0: print(currentCharIdx)

  
print(getCheckSum(diskList))
