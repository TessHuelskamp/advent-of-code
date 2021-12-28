import { readFileSync } from 'fs';

// file reading and writing
const file = readFileSync('./input.txt', 'utf-8');
const arr = file.toString().replace(/\r\n/g,'\n').split('\n');
const inputs = arr.map(Number)

function numGreaterThan(input: Array<number>): number {
    let numGreaterThan = 0;

    // IDK why the "for of" concept returns indicies that are strings :(
    for(let i=1; i < input.length; i++){
        if ( input [i-1] < input[i]){
            numGreaterThan +=1
        }
    }

    return numGreaterThan;
}

function moveIntoThrees(input: Array<number>): Array<number> {
    let numGreaterThan = 0;
    let result = new Array<number>();

    for(let i=2; i < input.length; i++){
       let sum = input[i-2] + input [i-1] + input[i];
       // this is probs not the best way to work with arrays :)
       result.push(sum)
    }

    return result;

}

// 1593
const partOneResult = numGreaterThan(inputs)
console.log(partOneResult)


let filtered = moveIntoThrees(inputs)

// 1597
const partTwoResult = numGreaterThan(filtered)
console.log(partTwoResult)



