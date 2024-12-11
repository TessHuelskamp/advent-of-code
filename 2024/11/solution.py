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


blinks = 0



# Surely, this should only take a few hours... :p
while blinks < 75:
  blinks +=1

  
  newStones = list()

  for stone in stones:
    left, right = unpack(stone)
    newStones.append(left)
    if right != None: newStones.append(right)

  stones = newStones

  if blinks == 25:
    print("part 1: ", len(stones))

  print(blinks)

  


print(len(stones))

