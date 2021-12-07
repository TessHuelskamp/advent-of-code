lines=list()
with open("./input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

from copy import copy

allPassports=list()
currentPassport=dict()
for line in lines:
    if len(line) == 0:
        allPassports.append(copy(currentPassport))
        currentPassport = dict()
    else:
        fields=line.split(" ")
        for field in fields:
            key, val = field.split(":")
            currentPassport[key]=val

if len(currentPassport) != 0:
    allPassports.append(copy(currentPassport))


FIELDS=["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
def inrange(left, val, right):
    return left <= val <= right

def isValid(passport):
    for field in FIELDS:
        if field not in passport:
            return False

    byr = int(passport["byr"])
    if not inrange(1920, byr, 2002):
        print("byr", byr)
        return False

    iyr = int(passport["iyr"])
    if not inrange(2010, iyr, 2020):
        print("iyr", iyr)
        return False

    eyr = int(passport["eyr"])
    if not inrange(2020, eyr, 2030):
        print("eyr", eyr)
        return False

    hgt = passport["hgt"]
    if "c" in hgt:
        hgt, _ = hgt.split("c")
        if not inrange(150, int(hgt), 193):
            print("chgt", hgt)
            return False
    elif "i" in hgt:
        hgt, _ = hgt.split("i")
        if not inrange(59, int(hgt), 76):
            print("ihgt", hgt)
            return False
    else:
        print("nohgt", hgt)
        return False

    hcl = passport["hcl"]
    if hcl[0] != "#":
        print("hcl bad format", hcl)
        return False
    hcl = hcl[1:]
    if len(hcl) != 6:
        print("hcl too short", hcl)
        return False
    for c in hcl:
        correct="0123456789abcdef"
        if c not in correct:
            print("hcl non alpha", hcl)
            return False

    ecl = passport["ecl"]
    if ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        print("ecl", ecl)
        return False

    pid = passport["pid"]
    if len(pid) != 9:
        print("pid too short", pid)
        return False
    try:
        int(pid)
    except ValueError:
        print("pid non alpha", pid)
        return False

    return True

totalGood = 0
for p in allPassports:
    if isValid(p):
        totalGood+=1

print(totalGood)
