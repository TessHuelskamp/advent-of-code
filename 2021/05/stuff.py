import numpy as np

with open("./input.txt", "r") as f: lines = f.readlines()

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return "({},{})->({},{})".format(self.x1, self.y1, self.x2, self.y2)

    def getMin(self):
        return min(self.x1, self.y1, self.x2, self.y2)
    def getMax(self):
        return max(self.x1, self.y1, self.x2, self.y2)

    def getMinX(self):
        return min(self.x1, self.x2)
    def getMaxX(self):
        return max(self.x1, self.x2)

    def getMinY(self):
        return min(self.y1, self.y2)
    def getMaxY(self):
        return max(self.y1, self.y2)

    def getSlope(self):
        if (self.x1 - self.x2) == 0:
            return 100
        else:
            return float(self.y1 - self.y2) / float(self.x1 - self.x2)

    def isVertical(self):
        return self.y1 == self.y2
    def isHorizontal(self):
        return self.x1 == self.x2
    def isNeg45(self):
        return -1.01 < self.getSlope() < -.99
    def isPos45(self):
        return .99 < self.getSlope() < 1.01

class Grid:
    def __init__(self, lines):
        self.lines=list()
        i = 0
        for line in lines:
            i+=1
            left, _, right = line.strip().split(" ")
            x1, y1 = (int(p) for p in left.split(","))
            x2, y2 = (int(p) for p in right.split(","))
            self.lines.append(Line(x1, y1, x2, y2))

        self.maxX = max(l.getMaxX() for l in self.lines)
        self.maxY = max(l.getMaxY() for l in self.lines)


        self.board=np.zeros((self.maxX+1, self.maxY+1), dtype=int)

    def calculateStraightLines(self):
        for line in self.lines:
            if line.isVertical():
                y = line.y1
                x1, x2 = line.x1, line.x2
                # swap in the case that our point isn't formatted "nicely"
                if x1 > x2:
                    x1, x2 = x2, x1
                for x in range(x1, x2+1):
                    self.board[x][y] += 1

            elif line.isHorizontal():
                x = line.x1
                y1, y2 = line.y1, line.y2
                if y1 > y2:
                    y1, y2 = y2, y1
                for y in range(y1, y2+1):
                    self.board[x][y] += 1

        return self.getNumDangerous()

    def getNumDangerous(self):
        rows, cols = np.where(self.board >= 2)
        assert len(rows) == len(cols)
        return len(rows)

    def addInDiagonalLines(self):
        # Assumes that the straight lines are already done

        for line in self.lines:
            if line.isPos45():
                x1, x2 = line.x1, line.x2
                y1, y2 = line.y1, line.y2

                if x1 > x2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1

                difference = x2-x1
                assert difference > 0
                for i in range(difference+1):
                    self.board[x1+i][y1+i] += 1
            elif line.isNeg45():
                x1, x2 = line.x1, line.x2
                y1, y2 = line.y1, line.y2
                if x1 < x2:
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1

                difference = x1 - x2
                assert difference > 0
                for i in range(difference+1):
                    self.board[x1-i][y1+i] += 1


        return self.getNumDangerous()



    def __repr__(self):
        return str(self.lines)


grid = Grid(lines)
res = grid.calculateStraightLines()
print(res)
res2 = grid.addInDiagonalLines()
print(res2)
