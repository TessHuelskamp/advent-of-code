debug = False
addingRules=True

rules={}

def addRule(left, right):
  if left not in rules:
    rules[left]=set()
  
  rules[left].add(right)

def fixRow(row):
  while not rowValid(row):
    # loop thru the row swapping errors as we find them

    left=set()

    for i, val in enumerate(row):
      currentRules = set()
      if val in rules:
        currentRules=rules[val]
    
      if currentRules.intersection(left):
        swapVal = currentRules.intersection(left).pop()
        j = row.index(swapVal)

        row[i]=swapVal
        row[j]=val

        break
      
      left.add(val)

  return row


def rowValid(row):
  left=set()

  for val in row:
    currentRules = set()
    if val in rules:
      currentRules=rules[val]
  
    if currentRules.intersection(left):
      return False
  
    left.add(val)

  return True



partOne = 0
partTwo = 0
  

with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    if not line:
      addingRules = False
      continue

    if addingRules:
      addRule(*line.split("|"))
      continue

    
    row = line.split(",") 
    correctOrder = rowValid(row)

    halfIdx = int(len(row)/2)
    if correctOrder:
      partOne+=int(row[halfIdx])
    else:
      newRow = fixRow(row)
      partTwo+=int(newRow[halfIdx])

    
print(partOne)
print(partTwo)


    


  
