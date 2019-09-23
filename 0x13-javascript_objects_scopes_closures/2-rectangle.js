#!/usr/bin/node
// Defining class 'Rectangle' with constructor and 2 declared attributes
// Empty obj created if either constructor attributes less than 0

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
