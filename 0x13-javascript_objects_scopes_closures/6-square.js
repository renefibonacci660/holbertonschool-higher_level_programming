#!/usr/bin/node
// New Square class that inherits from Square class in another file
// Added instance method that prints rectangle
// Super in constructor allows inheritence of Rectangle constructor attr

const Sqr = require('./5-square');

class Square extends Sqr {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let ArgvNum = 0; ArgvNum < this.height; ArgvNum++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
