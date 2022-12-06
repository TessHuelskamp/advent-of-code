from collections import Counter

with open("2022/06/input.txt", "r") as f:
    lines = f.readlines()

stuff = [x for x in lines[0]]

print(stuff[0:4])

for i in range(len(stuff)-14):
    next_four = stuff[i: i+14]
    set_four = set(x for x in next_four)

    if len(set_four) == 14:
        print(i+14)
        break
    
