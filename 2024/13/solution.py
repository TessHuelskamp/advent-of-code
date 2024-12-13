import re
import numpy as np
import math

debug = False

configs  = []

info = dict()

# Button A: X+20, Y+75
# Button B: X+93, Y+70
regex = r"Button [AB]: X\+([0-9]+), Y\+([0-9]+)"


with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  for line in f.readlines():
    line = line.strip()
    if "A" in line:
      match = re.search(regex, line)
      info["ax"]=int(match.group(1))
      info["ay"]=int(match.group(2))
    elif "B" in line:
      match = re.search(regex, line)
      info["bx"]=int(match.group(1))
      info["by"]=int(match.group(2))
    elif "P" in line:
       match = re.search(r"Prize: X=([0-9]+), Y=([0-9]+)", line)
       info["x"] = int(match.group(1))
       info["y"] = int(match.group(2))
    elif line == "":
      configs.append(info)
      info = dict()

configs.append(info)



def solve(info, partOne=True):
  """
  ax *a + bx*b = x
  ay *a + by*b = y
  """

  a = np.array([[info["ax"], info["bx"]], [info["ay"], info["by"]]])
  b = np.array([info["x"], info["y"]])

  vals = np.linalg.solve(a,b)

  
  # sometimes 14. was getting truncated to 13
  a, b = [int(round(x)) for x in vals]

  xLoc = info["ax"]*a + info["bx"]*b
  yLoc = info["ay"]*a + info["by"]*b

  if partOne and (a >100 or b>100):
    return 0
  elif xLoc == info["x"] and yLoc == info["y"]:
    return 3*a + b
  else:
    return 0


def solvePartTwo(info):
  delta = 10000000000000

  info["x"] += delta
  info["y"] += delta

  return solve(info, partOne=False)


partOne = 0
partTwo = 0

for stuff in configs:
  partOne += solve(stuff)
  partTwo += solvePartTwo(stuff)

print(partOne)
print(partTwo)

  