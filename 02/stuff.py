with open("./input.txt", "r") as f:
    horz, vert = 0, 0 
    aim = 0

    for line in f:
        direction, right = line.strip().split(" ")
        distance = int(right)

        if direction == "forward":
            horz += distance
            vert += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance

    print(horz * vert)
