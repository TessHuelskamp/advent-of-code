allNums=set()
with open("./input.txt", "r") as f:
    for line in f.readlines():
        allNums.add(int(line))
print(allNums)
print(len(allNums))

for num1 in allNums:
    total = 2020 - num1
    for num2 in allNums:
        if num2 == num1:
            continue
        opp = total - num2

        if opp == num1 or opp == num2:
            continue

        if opp in allNums:
            print(opp*num1*num2)
