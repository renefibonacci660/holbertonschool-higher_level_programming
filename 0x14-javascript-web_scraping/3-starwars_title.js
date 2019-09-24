#!/usr/bin/node
// Prints title of Star Wars Episode given in commandline with GET request

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
