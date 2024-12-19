debug = False
import functools

towels = set()
requests = list()

with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  for i, line in enumerate(f.readlines()):
    line = line.strip()

    if i==0:
      towels = {x.strip() for x in line.split(",")}
      continue

    if not line: continue
    requests.append(line)

print(towels)

@functools.cache
def valid(request):
  # exiting early here messes me up
  total = 0
  if request in towels: total+= 1

 

  for i in range(1, len(request)):
    left, right = request[:i], request[i:]
    
    if left in towels:
      rightTotal = valid(right)
      total+= rightTotal


  return total


partONe = 0
partTwo = 0
for request in requests:
  
  result = valid(request)
  print(request, result)

  if result: partONe +=1
  partTwo+= result


print(partONe)
print(partTwo)