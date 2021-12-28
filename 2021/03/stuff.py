lines=list()
with open("./input.txt", "r") as f:
    for line in f.readlines(): lines.append(line.strip()) 
gamma=""
ep=""

total0=list()
total1=list()
lenStuff=len(lines[0])
for i in range(len(lines[0])):
    total0.append(0)
    total1.append(0)

for line in lines:
    for i, val in enumerate(line):
        if val == "1":
            total1[i]+=1
        else:
            total0[i]+=1

for i, val0 in enumerate(total0):
    val1 = total1[i]

    if val0 > val1:
        gamma+="1"
        ep+="0"
    else:
        gamma+="0"
        ep+="1"

gamma_dec = int(gamma, 2)
ep_dec = int(ep, 2)

print(gamma_dec * ep_dec)


o2rating=0
co2rating=0



from copy import copy
oxygenRatings=copy(lines)
i=0
while len(oxygenRatings) > 1:
    num0, num1 = 0, 0
    for line in oxygenRatings:
        if line[i] == "1":
            num1+=1
        else:
            num0+=1
    
    newOxygenRatings = list()

    if num1 >= num0:
        # filter out all with 0
        for line in oxygenRatings:
            if line[i]=="1":
                newOxygenRatings.append(line)
    else:
        for line in oxygenRatings:
            if line[i]=="0":
                newOxygenRatings.append(line)
    i+=1
    oxygenRatings=copy(newOxygenRatings)

o2Rating=oxygenRatings[0]

co2Ratings=copy(lines)
i=0
while len(co2Ratings) > 1:
    num0, num1 = 0, 0
    for line in co2Ratings:
        if line[i] == "1":
            num1+=1
        else:
            num0+=1
    newco2Ratings = list()
    if num0 <= num1:
        keep="0"
    else:
        keep="1"
    for line in co2Ratings:
        if line[i]==keep:
            newco2Ratings.append(line)

    co2Ratings=copy(newco2Ratings)
    i+=1

co2Rating=co2Ratings[0]
print(co2Rating, o2Rating)
print(int(co2Rating, 2) * int(o2Rating, 2))
