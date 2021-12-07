with open("./input.txt", "r") as f:
    crabs = [int(x) for x in f.readline().strip().split(",")]


# didn't need to sort this but it works :)
crabs_sorted=sorted(crabs)


the_min = min(crabs_sorted)
the_max = max(crabs_sorted)

def fuelCost(distance):
    return int(distance/2.0 * (1 + distance))

assert fuelCost(1) == 1
assert fuelCost(2) == 3
assert fuelCost(5) == 15


best=100000000000000000000000
idx=0
for i in range(the_min, the_max+1):
    fuel=0
    for crab in crabs_sorted:
        fuel+=fuelCost(abs(i-crab))


    if fuel<best:
        best = fuel
        idx=i
    
print(best)
print(idx)
