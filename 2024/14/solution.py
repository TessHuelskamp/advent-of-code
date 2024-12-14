import re

from collections import namedtuple

Robot = namedtuple('Robot', ['x', 'y','vx', 'vy'])

robots = []

debug = False

w, h = 101, 103

if debug: w, h = 11, 7

# This is the dividing line. we dont care about anyone ON these lines
wHalf, hHalf = w//2, h//2


rounds = 100

board = [ list("."*w) for _ in range(h)]

# print(len(board), len(board[0]))

def printBoard(board):
  for line in board:
    print("".join([str(x) for x in line]))


with open("./input.sample.txt" if debug else "./input.txt", "r") as f:
  # p=0,4 v=3,-3
  # p=x,y v=vx,vy
  for line in f.readlines():
    match = re.search("p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)", line)

    x, y = int(match.group(1)), int(match.group(2))
    vx, vy = int(match.group(3)), int(match.group(4))

    robots.append(Robot(x, y, vx, vy))

def runRound(rounds, showBoard=False):
  q1, q2, q3, q4 = 0, 0, 0, 0

  board = [ list("."*w) for _ in range(h)]

  for robot in robots:

    xFinal = (robot.x + rounds * robot.vx) % w
    yFinal = (robot.y + rounds * robot.vy) % h

    board[yFinal][xFinal] = "x"

    if xFinal < wHalf and yFinal < hHalf:
      q1 +=1
    elif xFinal < wHalf and yFinal > hHalf:
      q2+=1
    elif xFinal > wHalf and yFinal < hHalf:
      q3+=1
    elif xFinal > wHalf and yFinal > hHalf:
      q4+=1
    else:
      # print(wHalf, hHalf)
      # print(xFinal, yFinal)
      pass

  
  if showBoard: printBoard(board)

  return q1*q2*q3*q4



minSafety = None
safetyI = None

for i in range(w*h+100):
  safety = runRound(i)

  # I'm not gonna lie, I went on reddit to figure out how to search for this
  if not minSafety or safety < minSafety:
    minSafety = safety
    safetyI = i


runRound(safetyI, showBoard=True)
print("part1 ", runRound(100))
print("part2 ", safetyI)




