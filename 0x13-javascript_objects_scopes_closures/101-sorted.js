#!/usr/bin/node

const dictionary = require('./101-data.js').dict;
const dict = {};
for (const key in dictionary) {
  dict[dictionary[key]] = [];
}
for (const key in dictionary) {
  dict[dictionary[key]].push(key);
}

console.log(dict);
