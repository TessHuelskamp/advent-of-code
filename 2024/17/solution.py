debug = True
debugFile = ''
write = False


regs = dict()
instructions = []

with open("./input."+debugFile+".txt" if debugFile else "./input.txt", "r") as f:
  for i, line in enumerate(f.readlines()):
    if i <= 2:
      _, val = line.split(":")
      val = int(val)
      
      if i == 0: reg = 'a'
      elif i ==1: reg = 'b'
      elif i ==2: reg = 'c'

      regs[reg] = val
    
    if i == 4:
      _, vals = line.split(":")
      instructions = [int(x) for x in vals.split(",")]

def runProgram(a, b, c):
  pointer = 0
  outputs = []

  regA, regB, regC = a, b, c

  while pointer <len(instructions)-1:
    opCode, literalOperand = instructions[pointer], instructions[pointer+1]

    comboOperand = literalOperand
    if literalOperand == 4: comboOperand = regA
    elif literalOperand == 5: comboOperand = regB
    elif literalOperand == 6: comboOperand = regC
    elif literalOperand == 7:
      print("wtf")
      exit()
    
    if opCode == 0: # adv
      regA = int(regA / 2**comboOperand)
    elif opCode == 1: #bxl xor for b
      regB = (regB%8) ^ (literalOperand%8)
    elif opCode == 2: # bst
      regB = (comboOperand % 8)
    elif opCode == 3: # jnz
      if regA != 0:
        pointer = literalOperand
        continue
    elif opCode == 4: #bxc
      regB = regB ^ regC
    elif opCode == 5: # out
      outputs.append(comboOperand%8)

    elif opCode == 6: # bdv
      regB = int(regA / 2**comboOperand)
    elif opCode == 7: #cdv
      regC = int(regA / 2**comboOperand)
    else:
      print(pointer)
      print(opCode, comboOperand)
      print("wtf ???")
      exit()

    pointer+=2
 

  return outputs

def findPartTwo():
  answers = [0]

  for j in range(len(instructions)):
    nextAnswers = []
    
    # build up program from reverse
    wantedIndex = len(instructions)-1-j
    wanted = instructions[wantedIndex:]

    # multiple values can get us to a particular substring
    # we want to record all options incase a later path fails
    for answer in answers:  
      answer = answer << 3
      for i in range(8+1):
        result = runProgram(answer+i, 0, 0)

        if result == wanted:
          nextAnswers.append(answer+i)
    
    answers = nextAnswers

  return min(answers)

partOne = runProgram(regs["a"], regs["b"], regs["c"])
print("part1: ", ','.join([str(x) for x in partOne]))


partTwo = findPartTwo()
print("part2: ", partTwo)
print(runProgram(partTwo, 0, 0))

  