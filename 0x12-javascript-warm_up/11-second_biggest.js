#!/usr/bin/node
// Searches the second biggest integer in the list of arguments
const MyArray = process.argv.slice(2);
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  console.log(MyArray.sort(function (a, b) { return b - a; })[1]);
}
