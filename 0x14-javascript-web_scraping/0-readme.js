#!/usr/bin/node
// Reads and prints the content of a file
// Requires fs module where readFile function is defined.
// Reading data in utf-8 format
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
