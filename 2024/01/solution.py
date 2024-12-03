from collections import Counter


listOne = list()
listTwo = list()

with open("./input.txt", "r") as f:
  for line in f.readlines():
    left, _, _, right = line.strip().split(" ")

    listOne.append(int(left))
    listTwo.append(int(right))

# Sorting is in place

listOne.sort()
listTwo.sort()

partOne = 0
partTwo = 0

myCounter = Counter(listTwo)

for i, listOneVal in enumerate(listOne):
  listTwoVal = listTwo[i]

  partOne += abs(listOneVal -listTwoVal)
  # Counter defaults to zero
  partTwo += ( myCounter[listOneVal] * (listOneVal))

print(partOne)

print(partTwo)













