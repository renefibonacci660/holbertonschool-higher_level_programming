#!/usr/bin/node
// Returns reversed version of given list without built-in reverse

exports.esrever = function (list) {
  for (var element = 0; element <= ((list.length - 1) / 2); element++) {
    const rev = list[element];
    list[element] = list[list.length - 1 - element];
    list[list.length - 1 - element] = rev;
  }
  return list;
};
