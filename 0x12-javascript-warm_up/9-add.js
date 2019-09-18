#!/usr/bin/node
// Prints addition of two ints passed into a function
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(process.argv[2], process.argv[3]);
