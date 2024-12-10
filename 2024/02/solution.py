



def levelValidOne(level):
  levelCopy = [x for x in level]

  levelSorted = [x for x in levelCopy]
  levelReversed = [x for x in levelCopy]

  # I wish that you could chain calls in python :(
  levelSorted.sort()
  levelReversed.sort()
  levelReversed.reverse()

  if not (level == levelSorted or level == levelReversed):
    return False
  
  for i, val in enumerate(level):
    if i==0: continue
    prevVal = level[i-1]

    diff = abs(val - prevVal)
    if 1 <= diff <= 3:
      continue
    else:
      return False
  
  return True
  

  


partOne = 0
partTwo = 0

with open("./input.txt", "r") as f:
  for line in f.readlines():
    level = [ int(x) for x in line.strip().split(" ")]
   


    
    if levelValidOne(level):
      partOne+=1
      partTwo+=1
      continue


    # find the offending thing in the list. Remove it and see what happens

    
    # This has rough run time complexity buuutttt.....
    # It works and it's easier that computing where the error is and trying to correct it
    valid=False
    for i in range(len(level)):
      if valid: break
      
      if levelValidOne(level[0:i]+level[i+1:]):
        partTwo+=1
        valid=True
        

print(partOne)
print(partTwo)
