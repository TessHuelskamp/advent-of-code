import re
lines=list()

digits = list()


def firstDigit(s):
	return int([x for x in s if x in "0123456789"][0])
	
with open("./input.txt", "r") as f:
	for line in f.readlines(): 
		forward = line.strip()
		backward = forward[::-1]

		digits.append(firstDigit(forward)*10 + firstDigit(backward))


print(sum(digits))



