#!/usr/bin/node
// Printing multiple passed in argv with let vars
let FirstArg = 'undefined';
let SecArg = 'undefined';

if (process.argv[2]) {
  FirstArg = process.argv[2];
}
if (process.argv[3]) {
  SecArg = process.argv[3];
}
console.log(FirstArg, 'is', SecArg);
