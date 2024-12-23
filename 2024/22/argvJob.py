debugFile = ''
debug = bool(debugFile)

initalSecrets = []
with open("./input."+debugFile+".txt" if debugFile else "./input.txt", "r") as f:
  initalSecrets = [int(x) for x in f.readlines()]


def genNextSecret(secret):
  MOD = 16777216
  secret ^= (secret*64)
  secret %= MOD
  secret ^= int(secret/32)
  secret %= MOD
  secret ^= secret*2048
  secret %= MOD

  return secret


def gen2000(secret):
  results=[secret]
  for _ in range(2000):
    secret = genNextSecret(secret)
    results.append(secret)
    
  return results

allSecrets = [gen2000(x) for x in initalSecrets]
partOne = sum(x[-1] for x in allSecrets)
print(partOne)

def getPrices(myList):
  return [x%10 for x in myList]

def getDifferences(myList):
  res = []
  for i, val in enumerate(myList):
    if i == 0:
      res.append(None)
      continue

    res.append(val-myList[i-1])

  return res



# Sanity checking
# firstSecrets = gen2000(123)
# firstPrices  = getPrices(firstSecrets)
# firstDifferences = getDifferences(firstPrices)

# for i in range(10):
#   secret = firstSecrets[i]
#   price = firstPrices[i]
#   difference =  firstDifferences[i]
#   print(f"{secret:10}: {price} ({difference})")
  
import itertools
import functools

allPrices = tuple(getPrices(x) for x in allSecrets)
allDifferences = tuple(getDifferences(x) for x in allPrices)

@functools.lru_cache(maxsize=2050*3*3*100)
def findShortSequence(seq, myList):
  for i in range(len(myList) - len(seq)+1):
    subset = myList[i:i+len(seq)]
    
    if subset == seq: return True

  return False


def findSequence(seq, myList):
  seq = tuple(seq)

  # check if short sequences present to save some time
  if not findShortSequence(seq[:3], myList) or not findShortSequence(seq[1:], myList):
    return None

  for i in range(len(myList) - len(seq)+1):
    subset = myList[i:i+len(seq)]
    
    if subset == seq: return i

  return None

def findValues(allPrices, allDifferences, combo, maxFound):
  total = 0
  for i, prices in enumerate(allPrices):
   
    differences = allDifferences[i]

    idx = findSequence(combo, tuple(differences))
    if idx:
      # We buy the last value when we see the sequence
      total += prices[idx+3]

    
    # exit early if theres no way to beat the best thing weve found
    # if 9*(len(allPrices)-i) < maxFound:
    #   return total

    
  return total


ordering = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

def scoreCombo(combo):
  return ''.join(chr(ord('a')+ordering.index(x)) for x in combo)


# max found so far
# 1787 (1, -2, 1, 1)
# 1802 (2, -1, -1, 2)
partTwo = 1802


import sys
beginning = sys.argv[1]
end = sys.argv[2]


firstVal = ordering[0]

i=0
for combo in itertools.product(ordering, repeat=4):
  if beginning <= scoreCombo(combo) and scoreCombo(combo) <= end:
    pass
  else:
    continue
 
  i+=1

  if i%(len(ordering)**2) == 0: print(combo)

  if firstVal != combo[0]:
    print('answer: ', partTwo, combo)
    firstVal = combo[0]

  total = findValues(allPrices, allDifferences, combo, partTwo)


  if total > partTwo:
    partTwo = total
    print(partTwo, combo)

print(partTwo)


# Generate prices

  
print('done')