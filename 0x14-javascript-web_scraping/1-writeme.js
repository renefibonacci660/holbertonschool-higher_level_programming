#!/usr/bin/node
// Writing a string to a file given in command line
// Requires fs module where 'writeFile' function is defined
const fs = require('fs');

const data = process.argv[3];

fs.writeFile(process.argv[2], data, 'utf8', (err) => {
  if (err) throw err;
});
