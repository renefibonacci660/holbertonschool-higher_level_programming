#!/usr/bin/node
// Learning to use isNaN and to parse an Int of passed argv
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
