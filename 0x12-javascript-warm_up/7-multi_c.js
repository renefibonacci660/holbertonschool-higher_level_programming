#!/usr/bin/node
// Using for loop / isNaN / parseInt in tantem
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let ArgvNum = 0; ArgvNum < (parseInt(process.argv[2])); ArgvNum++) {
    console.log('C is fun');
  }
}
