from enum import Enum

with open("./input.txt", "r") as f:
    lines = f.readlines()

class Instruction(Enum):
    ACC = "acc"
    JMP = "jmp"
    NOP = "nop"

class CPU:
    def __init__(self, lines):
        self.acc = 0
        self.idx = 0
        self.instructions=list()

        for line in lines:
            instruction, value = line.split(" ")
            self.instructions.append((Instruction(instruction), int(value)))

    def __repr__(self):
        res  = "acc {}\n".format(self.acc)
        res += "idx {}\n".format(self.idx)
        res += str(self.instructions)

        return res

    def run(self):
        self._reset()
        lines_run = set()

        while self.idx not in lines_run:
            if self.idx >= len(self.instructions):
                return self.acc, True

            lines_run.add(self.idx)
            instruction, amount = self.instructions[self.idx]

            if instruction == Instruction.ACC:
                self.acc += amount
                self.idx +=1
            elif instruction == Instruction.NOP:
                self.idx +=1
            elif instruction == Instruction.JMP:
                self.idx += amount

        return self.acc, False

    def _reset(self):
        self.acc = 0
        self.idx = 0


    def findError(self):
        for i in range(len(self.instructions)):
            instruction, amount = self.instructions[i]

            # modify in place
            if instruction == Instruction.NOP:
                self.instructions[i]=(Instruction.JMP, amount)
            elif instruction == Instruction.JMP:
                self.instructions[i]=(Instruction.NOP, amount)
            else:
                continue

            # try it out 
            acc, exits = self.run()

            if exits:
                return acc

            # if it doesn't work put it back
            self.instructions[i]=(instruction, amount)


cpu = CPU(lines)
value, _ = cpu.run()
print(value)

new_acc=cpu.findError()
print(new_acc)


