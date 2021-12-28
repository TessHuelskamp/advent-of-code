from collections import Counter

with open("input.txt", "r") as f:
    lines = f.readlines()

template = lines[0].strip()


rules = dict()
for line in lines[2:]:
    left, _, right = line.strip().split(" ")
    rules[left]=right


def polymer(template, count):
    if count == 0:
        return template

    nextTemplate = template[0]

    for i, val in enumerate(template):
        if i==0:
            continue

        pair = template[i-1] + val

        match = rules.get(pair, count-1)
        if match:
            nextTemplate += match

        nextTemplate += val

    template = nextTemplate

    return polymer(template, count-1)


from functools import lru_cache

@lru_cache(maxsize=26*26*40)
def polymer2(template, count):
    if count==0:
        return Counter(template)

    total = Counter()
    template = polymer(template, 1)
    for i, val in enumerate(template):
        if i==0:
            continue

        pair = template[i-1]+val
        res = polymer2(pair, count-1)
        total += res

    # remove thigns we've counted twice (everything that's not at the ends)
    for val in template[1:len(template)-1]:
        total[val] -= 1

    return total





result10 = polymer(template, 10)
c = Counter(result10)
diff = max(c.values()) - min(c.values())
assert diff == 2375
print(diff)

# check that the recursive solution works the same as the OG-naive one :)
result10Rec = polymer2(template, 10)
for key, value in c.items():
    assert key in result10Rec
    assert value == result10Rec[key]

r40 = polymer2(template, 40)
diff40 = max(r40.values()) - min(r40.values())
print(diff40)
