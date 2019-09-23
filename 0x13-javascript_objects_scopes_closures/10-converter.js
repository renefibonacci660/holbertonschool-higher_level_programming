#!/usr/bin/node
//Converts number to given base without declaring new var

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
