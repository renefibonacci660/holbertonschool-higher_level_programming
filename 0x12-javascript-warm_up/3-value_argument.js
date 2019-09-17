#!/usr/bin/node
// Showcasing how to print args passing in by commandline
if (process.argv[2]) {
  console.log('%s', process.argv[2]);
} else {
  console.log('No argument');
}
