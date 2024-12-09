import itertools


def eval(values, ops):
  total = values[0]

  for i, op in enumerate(ops):
    if op == "+":
      total += values[i+1]
    elif op == "*":
      total *= values[i+1]
    elif op == "|":
      total = int(str(total)+str(values[i+1]))
  
  return total


debug = False

partOne = 0
partTwo = 0

with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()

    total, equation = line.split(":")
    total = int(total)
    equationParts = equation.strip().split(" ")
    equationParts = [ int(x) for x in equationParts ]


    found = False

    for combo in itertools.product("+*", repeat=len(equationParts)-1):
      if total == eval(equationParts, combo):
        partOne += total
        partTwo += total
        found=True
        break

    if found: continue

    for combo in itertools.product("+*|", repeat=len(equationParts)-1):
      if total == eval(equationParts, combo):
        partTwo += total
        found=True
        break


    

print(partOne)
print(partTwo)

    


