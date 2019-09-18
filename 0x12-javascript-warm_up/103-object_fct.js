#!/usr/bin/node
// Updated this script by adding line 8;
// a new function incr that increments the integer value
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () { myObject.value++; };
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
