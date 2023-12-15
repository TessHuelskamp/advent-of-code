import re
lines=list()
digits = list()
digits2= list()


def firstDigit(s):
	return int([x for x in s if x in "0123456789"][0])

swaps = {
	"one": "o1e",
	"two": "t2o",
	"three": "t3e",
	"four": "f4r",
	"five": "f5e",
	"six": "s6x",
	"seven": "s7n",
	"eight": "e8t",
	"nine": "n9e",
}

def swapWords(l):

	search = True
	while search:
		search = False
		results = { x:9999 for x in swaps.keys()}

		for k in swaps.keys(): results[k] = l.find(k)
		for k, v in results.items():
			if v == -1:
				results[k] = 9999

		swapKey = min(results, key=results.get)
		
		#print(swapKey, results[swapKey], results)

		if results[swapKey] != 9999:
			search = True
			l =l.replace(swapKey, swaps[swapKey], 1)

	return l
		

with open("./input.txt", "r") as f:
	for line in f.readlines(): 
		forward = line.strip()
		backward = forward[::-1]

		subs = swapWords(forward)
		subBackward = subs[::-1]

		if forward != subs: print(forward, subs)


		digits.append(firstDigit(forward)*10 + firstDigit(backward))
		digits2.append(firstDigit(subs)*10 + firstDigit(subBackward))


print("basic ", sum(digits))
print(sum(digits2))
