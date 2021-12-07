with open("./input.txt", "r") as f:
    lines=[int(x) for x in f.readlines()]

class XMAS:
    def __init__(self, lines):
        self.lines = lines
    def __repr__(self):
        return str(self.lines)

    def walk(self):
        valid=True
        left=0
        right=24

        while valid:
            valid=False
            cache=set(self.lines[left:right+1])
            next_number=self.lines[right+1]

            for number in cache:
                pair = next_number - number
                if pair == number:
                    continue
                if pair in cache:
                    valid=True
                    break

            if not valid:
                return next_number

            left+=1
            right+=1

    def breakThing(self):
        total = self.walk()

        currentValue = 0
        left, right = 0, 0

        while currentValue != total:
            if currentValue < total:
                currentValue+=self.lines[right]
                right+=1
            elif currentValue > total:
                currentValue-=self.lines[left]
                left+=1

        numRange=self.lines[left:right+1]
        return min(numRange) + max(numRange)

xmas = XMAS(lines)
print(xmas.walk())
print(xmas.breakThing())
