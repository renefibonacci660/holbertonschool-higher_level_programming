#!/usr/bin/node
// Printing square size of second argv if int
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let ArgvNum = 0; ArgvNum < (parseInt(process.argv[2])); ArgvNum++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
