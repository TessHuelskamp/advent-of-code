import re


def multiply(string):
   # who knows why these are 1 based things but oh well....
  left = int(re.search(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", string).group(1))
  right = int(re.search(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", string).group(2))

  return left * right


def process(stuff):
  results = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", stuff)

  return sum([multiply(x) for x in results])


 


stuff = ''
with open("./input.txt", "r") as f:
  for line in f.readlines():
    stuff += line


partOne = process(stuff)
print(partOne)



# part two 

# Split on each "do". Treat that as a new program.
# Then for all of the dos we split on "don't() and do all of the muls for that"
# SPlit on the DO things. Then we know that all of them are good at the beginning.
# THen we split off of the don't() regex... we can grab the first one there

dos = re.split(r"do\(\)", stuff)

partTwo = 0
for do in dos:
  # Everything up until the first don't() is valid
  # That's the first thing in the list
  enabledInstructions = re.split(r"don't\(\)", do)[0]

  partTwo += process(enabledInstructions)


# 53783319
print(partTwo)






