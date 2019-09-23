#!/usr/bin/node
// Imports an array and computes a new array with increased multiplied values
const list = require('./100-data').list;
console.log(list);
console.log(list.map((index, multiple) => index * multiple));
