lines=list()
with open("./input.txt", "r") as f:
    for line in f.readlines():
        lines.append(line.strip())

allSeats=list()
highest=0
for seat in lines:
    row, seat = seat[:7], seat[7:]

    binary_row = row.replace("F", "0")
    binary_row = binary_row.replace("B", "1")

    binary_seat = seat.replace("L", "0")
    binary_seat = binary_seat.replace("R", "1")

    dec_row = int(binary_row, 2)
    dec_seat = int(binary_seat, 2)

    total = dec_row * 8 + dec_seat
    if total > highest:
        highest=total
    allSeats.append(total)

print(highest)

allSeats=sorted(allSeats)
for i, seat in enumerate(allSeats):
    nextSeat = allSeats[i+1]
    if seat +1 != nextSeat:
        print(seat +1)
        break

