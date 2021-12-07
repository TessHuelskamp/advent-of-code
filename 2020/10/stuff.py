with open("./input.txt", "r") as f:
    adapters  = [int(x) for x in f.readlines()]

adapters.append(0) # ground
adapters.append(max(adapters)+3) # device

sorted_list = sorted(adapters)
oneDiff, threeDiff = 0,0

for i, volt in enumerate(sorted_list):
    if i ==0: continue
    prev_volt = sorted_list[i-1]

    if volt - prev_volt == 3:
        threeDiff +=1
    elif volt - prev_volt == 1:
        oneDiff +=1
    else:
        print(i, volt, prev_volt)

print(oneDiff * threeDiff)


