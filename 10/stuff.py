import operator

with open("./input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

total=0
bad={
    ")":3,
    "]":57,
    "}": 1197,
    ">":25137
}
bad2={
    ")":1,
    "]":2,
    "}":3,
    ">":4,
}

pairs={
    "(":")",
    "[":"]",
    "{":"}",
    "<":">",
}

incomplete=list()
for line in lines:
    stack=list()
    valid=True
    for c in line:
        if c in set("({[<"):
            stack.append(c)
        elif c in set(")}]>"):

            pair = stack[-1]
            stack = stack[:-1]

            if pairs[pair] != c:
                valid=False
                total+=bad[c]
                break
    if not valid:
        continue

    if len(stack) == 0:
        # good line
        continue

    score=0
    missing = [ pairs[x] for x in reversed(stack)]

    for p in missing:
        score*=5
        score+=bad2[p]

    incomplete.append(score)

print(total)


incomplete=sorted(incomplete)
print(incomplete[len(incomplete)/2])
