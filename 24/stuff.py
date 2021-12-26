# lmao, sorry
def intOrString(x):
    try: return int(x)
    except ValueError: return x

with open("./input.txt", "r") as f:
    stuff = [ line.strip().split(" ") for line in f.readlines() ]

instructions = []
for line in stuff:
    thing = [ intOrString(x) for x in line ]
    instructions.append(thing)

class ALU:

    def __init__(self, instructions, debug=True):
        self.inst = instructions
        self.memory = self._getReset()

    def _getReset(self): return {"w":0, "x":0, "y":0, "z":0}
    def reset(self): self.memory = self._getReset()

    def run(self, modelNumber, debug=False):
        assert len(modelNumber) == 14

        modelIdx=0

        for line in self.inst:
            if debug:
                print(line, self.memory)
            rule = line[0]
            dest = line[1]

            if rule == "inp":
                self.set(dest, int(modelNumber[modelIdx]))
                modelIdx+=1
                continue

            # the rest of the instructions have 3 parts
            destVal = self.get(dest)
            amountOrReg = line[2]
            if isinstance(amountOrReg, str):
                amount = self.get(amountOrReg)
            else:
                amount = amountOrReg

            res = 0

            if rule == "add":
                res = destVal + amount

            elif rule == "mul":
                res = destVal * amount

            elif rule == "div":
                if amount == 0:
                    self.quit()
                    break
                res = int(destVal/amount)

            elif rule == "mod":
                if destVal < 0 or amount <=0:
                    self.quit()
                    break
                res = destVal % amount

            elif rule ==  "eql":
                res = 1 if destVal == amount else 0

            self.set(dest, res)


    def quit(self):
        self.set("z", -1)

    def set(self, key, val):
        assert key in "wxyz"
        self.memory[key] = val
    def get(self, key):
        assert key in "wxyz"
        return self.memory[key]

    def isValid(self):
        return self.get("z") == 0



alu = ALU(instructions)

def hasZero(number): return any( int(x)==0 for x in str(number))
assert hasZero(10)
assert hasZero(9009)
assert not hasZero(1234)

x = 99999998870000 + 1
while True:
    x -= 1

    if x % 10000 == 0:
        print("searching ", x)

    if hasZero(x):
        continue

    alu.run(str(x))
    if alu.isValid():
        break
print(x)
