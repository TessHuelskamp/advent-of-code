import * as fs from 'fs';

// file reading taken from one of my coworkers
let input = fs.readFileSync("./input.txt", "utf-8");
let lines = input.split('\n')

// part 1
let horz = 0;
let depth = 0;

for ( let line of lines) {
    let stuff = line.split(" ");
    let direction = stuff[0];
    // a fun type coercion thing :)
    let distance = +stuff[1]

    if (direction === "up") {
        depth -= distance;
    } else if (direction === "down") {
        depth += distance;
    } else if (direction === "forward") {
        horz+=distance;
    }
}

console.log(horz*depth)


// part 2
let horz2=0;
let depth2=0;
let aim2=0;

// TODO: learn what this syntax means in depth :)
lines.forEach(line => {
    let stuff = line.split(" ");
    let direction = stuff[0];
    // a fun type coercion thing :)
    let distance = +stuff[1]

    if (direction === "up") {
        aim2 -= distance;
    } else if (direction === "down") {
        aim2 += distance;
    } else if (direction === "forward") {
        horz2 += distance;
        depth2 += aim2 * distance;
    }
})

console.log(horz2 * depth2)


