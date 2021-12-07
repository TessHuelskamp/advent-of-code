from functools import lru_cache

lanternFish=list()
with open("./input.txt", "r") as f:
    lanternFish=[int(x) for x in f.readline().strip().split(",")]


# Exponential growth will take forever :)
# Do a cached DFS to see how many fish ONE lanternfish will spawn
# Lets do a depth first search to see how many lanternfish will be there on day 80
# Cache size is unbounded here :)
@lru_cache(maxsize=80*8)
def individualFish(timer, day):
    if day==0:
        return 1

    timer-=1
    day-=1
    if timer==-1:
        return individualFish(8, day) + individualFish(6, day)
    else:
        return individualFish(timer, day)

def listOfFish(fishes, days=80):
    return sum(individualFish(fish, days) for fish in fishes)

og_input = [3,4,3,1,2]
og_days = 18
og_answer = 26
og_days_large=80
og_answer_large=5934

assert listOfFish(og_input, og_days) == og_answer
assert listOfFish(og_input, og_days_large) == og_answer_large
print(listOfFish(lanternFish, og_days_large))
print(listOfFish(lanternFish, 256))
