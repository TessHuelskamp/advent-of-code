import copy

debugFile = ''
debug = bool(debugFile)

keys = list()
locks = list()

def processThing(lines):
  rows = [0, 0, 0, 0, 0]
  for line in lines:
    for i, char in enumerate(line):
      if char == "#": rows[i] +=1
  return rows


with open("./input."+debugFile+".txt" if debugFile else "./input.txt", "r") as f:
  while True:
    line = f.readline()
    line = line.strip()

    # EOF
    if not line: break

    isKey = True if line == "#####" else False

    lines = [f.readline() for _ in range(5)]
    row = processThing(lines)

    if isKey:
      keys.append(copy.copy(row))
    else:
      locks.append(copy.copy(row))
    
    # 7th row of lock/key that doesn't matter
    f.readline()

    # newline that also doesn't matter
    empty = f.readline().strip()

      

if debug:
  print("k", keys)
  print("l", locks)
  

partOne = 0
for key in keys:
  for lock in locks:
    correct = all( h + lock[i] <= 5 for i, h in enumerate(key))
    
    if correct: partOne +=1

print(partOne)
