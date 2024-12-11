import functools

debug = False

stones = []

with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  stones = [int(x) for x in f.readline().strip().split()]

def unpack(stone):
  if stone == 0:
    return 1, None
  elif len(str(stone))%2 ==0:
    stone=str(stone)
    half = int(len(stone)/2)
    left, right = stone[:half], stone[half:]

    return int(left), int(right)

  else:
    return stone * 2024, None
  

@functools.cache
def getBlinks(stone, blinks):
  if blinks == 0:
    return 1
  
  left, right = unpack(stone)

  if right != None:
    return getBlinks(left, blinks-1) + getBlinks(right, blinks-1)
  else:
    return getBlinks(left, blinks-1)


part1 = sum([getBlinks(x, 25) for x in stones])
part2 = sum([getBlinks(x, 75) for x in stones])

print(part1)
print(part2)