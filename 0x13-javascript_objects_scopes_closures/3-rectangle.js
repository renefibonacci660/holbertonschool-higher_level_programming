#!/usr/bin/node
// Defining class 'Rectangle' with constructor and 2 declared attributes
// Empty obj created if either constructor attributes less than 0
// Instance method 'print' prints square with contructor attributes

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ArgvNum = 0; ArgvNum < this.height; ArgvNum++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
