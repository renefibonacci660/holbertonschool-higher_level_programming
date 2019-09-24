#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileDest = process.argv[3];

request(url, function (err, response, body) {
  if (err) console.log(err);
  fs.writeFile(fileDest, body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
