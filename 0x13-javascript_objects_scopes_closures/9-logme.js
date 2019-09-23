#!/usr/bin/node
// Prints num of args already printed and new arg value

let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter += 1;
};
