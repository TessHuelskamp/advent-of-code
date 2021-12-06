import numpy
import itertools

lines=list()
with open("./input.txt", "r") as f:
    lines=[line.strip() for line in f.readlines()]

class Board:

    def __init__(self, lines):
        assert len(lines) == 5
        newlines=list()

        # this is the ugliest array code I've ever written :)
        # concat the lists together
        one_list = list(itertools.chain(x for x in lines))
        # make it a string
        one_string = " ".join(one_list)
        # remove dup spaces
        line=" ".join(one_string.split())
        # ints instaed of strings
        ints = map(int, line.split(" "))
        board = numpy.array(ints)
        self.board = board.reshape([5,5])

    def __repr__(self):
        return str(self.board) + "\n"

    def markNumber(self, number):
        found = numpy.squeeze(numpy.where(number == self.board))

        if found.size > 0:
            self.board[found[0]][found[1]] = 0

        return found.size > 0

    def getSum(self):
        # dont want to deal with radd to get sum to work :)
        return numpy.sum(self.board, keepdims=False)

    def getDiagSums(self):
        diag1 = [ (x, x) for x in range(5)]
        diag2 = [ (x, 4-x) for x in range(5)]
        diag1Sum = sum(self.board[entry[0], entry[1]] for entry in diag1)
        diag2Sum = sum(self.board[entry[0], entry[1]] for entry in diag2)
        return diag1Sum, diag2Sum

    def isWinner(self):
        results0 = numpy.sum(self.board, keepdims=False, axis=0)
        results1 = numpy.sum(self.board, keepdims=False, axis=1)

        allSums = list(itertools.chain(self.getDiagSums(), results1, results0))
        return any( x==0 for x in allSums)


class Boards:
    def __init__(self, lines):
        self.callout = [int(x) for x in lines[0].split(",")]
        self.boards = list()

        for i in range(2, len(lines), 6):
            self.boards.append(Board(lines[i:i+5]))

    def __repr__(self):
        res = " ".join(str(x) for x in self.callout) + "\n"
        for board in self.boards:
            res += str(board)
            return res

    def play(self):
        for number in self.callout:
            for board in self.boards:
                board.markNumber(number)
                if board.isWinner():
                    total=board.getSum()
                    print(total, number)
                    print(total * number)

                    return

    def play2(self):
        for number in self.callout:
            for board in self.boards:
                board.markNumber(number)

            if len(self.boards) > 1:
                self.boards = filter(lambda x: not x.isWinner(), self.boards)

            if len(self.boards) == 1:
                board = self.boards[0]
                if board.isWinner():
                    total=board.getSum()
                    print(total, number)
                    print(total * number)
                    return 

game2 = Boards(lines)
game2.play2()


game1 = Boards(lines)
game1.play()

