from itertools import product
from collections import Counter
from functools import lru_cache

p1Spot = 9
p2Spot = 10

p1Score, p2Score = 0, 0

def dice():
    while True:
        for x in range(1, 100+1):
            yield x
d = dice()

def move(start, amount):
    amount %= 10
    total  = start + amount
    if total > 10:
        total -= 10
    assert 1 <= total <= 10
    return total

assert move(10, 1) == 1
assert move(10, 2) == 2
assert move(2, 10) == 2
assert move(3, 7) == 10

# True is p1's turn
turn = True
numDiceRolls=0
while p1Score < 1000 and p2Score < 1000:


    roll = sum(next(d) for _ in range(3))
    numDiceRolls+=3

    if turn:
        p1Spot = move(p1Spot, roll)
        p1Score += p1Spot
    else:
        p2Spot = move(p2Spot, roll)
        p2Score += p2Spot

    turn ^= True


loser = min(p1Score, p2Score)
answer = loser * numDiceRolls
print(answer)
assert answer == 707784

####### PART 2 ######
# like a generator but its basically a static function
def diracRolls():
    rolls = product(range(1,4), range(1,4), range(1,4))
    return Counter(map(sum, rolls))

dice = diracRolls()
assert sum(x for x in dice.values()) == 3*3*3
assert dice[9] == 1
assert dice[3] == 1

@lru_cache(maxsize=10*22*10*22*2)
def playGame(p1Spot, p1Score, p2Spot, p2Score, turn):
    # returns number of wins p1Has and p2has

    p1Wins, p2Wins = 0, 0

    for roll, count in diracRolls().items():

        nextP1Spot, nextP1Score = p1Spot, p1Score
        nextP2Spot, nextP2Score = p2Spot, p2Score
        nextTurn = turn ^ True

        if turn:
            nextP1Spot = move(p1Spot, roll)
            nextP1Score += nextP1Spot
        else:
            nextP2Spot = move(p2Spot, roll)
            nextP2Score += nextP2Spot

        if nextP1Score >= 21:
            p1Wins += count
        elif nextP2Score >= 21:
            p2Wins += count
        else:
            p1Small, p2Small = playGame(nextP1Spot, nextP1Score, nextP2Spot, nextP2Score, nextTurn)

            p1Wins += p1Small * count
            p2Wins += p2Small * count

    return p1Wins, p2Wins

p1Wins, p2Wins = playGame(9, 0, 10, 0, True)
answer = max(p1Wins, p2Wins)
print(answer)
assert answer == 157595953724471
