with open("./input.txt", "r") as f:
    lines = f.readlines()

def sortString(s):
    return "".join(sorted(s))

total=0
for line in lines:
    left, right = line.strip().split("|")

    left=left.strip()
    right=right.strip()
    lwords=left.split(" ")
    rwords=right.split(" ")

    lens={4, 2, 3, 7}

    total+=sum(1 for x in rwords if len(x) in lens)


assert total == 390
print(total)


total=0
for line in lines:
    left, right = line.strip().split("|")

    lwords=left.strip().split(" ")
    rwords=right.strip().split(" ")

    lwords = [sortString(x) for x in lwords]
    rwords = [sortString(x) for x in rwords]

    found = dict()
    reverse = dict()

    for word in lwords:
        if len(word) == 2:
            found[word]=1
            reverse[1]=word
        elif len(word) == 4:
            found[word]=4
            reverse[4]=word
        elif len(word) == 3:
            found[word]=7
            reverse[7]=word
        elif len(word)==7:
            found[word]=8
            reverse[8]=word

    # missing
    # 2 3 5 6 9 0
    # have 1 4 7 8
    unseen = list(filter(lambda x: x not in found, lwords))
    assert len(unseen) == 6

    # 0, 6, and 9 all have 6 spots
    zero_six_nine = list(filter(lambda x: len(x)==6, unseen))
    assert len(zero_six_nine) == 3

    # six only has one intersection with 1
    six = list(filter(lambda x: len(set(x) & set(reverse[1]))==1, zero_six_nine))
    assert len(six) == 1
    six_word = six[0]
    found[six_word]=6
    reverse[6]=six_word

    # 9 is a superset of 4
    zero_nine = list(filter(lambda x: x not in found, zero_six_nine))
    assert len(zero_nine) == 2
    nine = list(filter(lambda x: set(x).issuperset(set(reverse[4])), zero_nine))
    zero = list(filter(lambda x: not set(x).issuperset(set(reverse[4])), zero_nine))
    assert len(nine) == 1
    assert len(zero) == 1
    nine_word=nine[0]
    zero_word=zero[0]

    found[nine_word]=9
    reverse[9]=nine_word
    found[zero_word]=0
    reverse[0]=zero_word

    # all that's left is 2 3 5
    missing = list(filter(lambda x: x not in found, lwords))
    assert len(missing) == 3

    # 3 has two intersections with 1
    three = list(filter(lambda x: len(set(x) & set(reverse[1])) == 2, missing))
    assert len(three) == 1
    three_word = three[0]
    found[three_word]=3
    reverse[3] = three_word

    missing = list(filter(lambda x: x not in found, lwords))
    assert len(missing) == 2

    topLeftPos = set(reverse[9]) - set(reverse[3])
    assert len(topLeftPos) == 1
    topLeftPos = topLeftPos.pop()

    five = list(filter(lambda x: topLeftPos in set(x), missing))
    two = list(filter(lambda x: not topLeftPos in set(x), missing))
    assert len(five) == 1
    assert len(two) == 1
    two_word = two[0]
    five_word = five[0]

    found[two_word]=2
    found[five_word]=5
    reverse[2]=two_word
    reverse[5]=five_word

    # build word now that we've found everything
    stringNum = "".join(map(lambda x: str(found[x]), rwords))
    total+=int(stringNum)

print(total)

assert total==1011785
