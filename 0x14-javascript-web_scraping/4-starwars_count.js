#!/usr/bin/node
// Prints num of movies where the character “Wedge Antilles” is present
// Accomplished by parsing thru GET body and checking for character 18 under film/people/18

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let films = 0;
    const Allfilms = JSON.parse(body).results;
    for (let num = 0; num < Allfilms.length; num++) {
      const characters = Allfilms[num].characters;
      for (let i = 0; i < characters.length; i++) {
        if (characters[i] === 'https://swapi.co/api/people/18/' || characters[i] === 'http://swapi.co/api/people/18/') {
          films += 1;
        }
      }
    }
    console.log(films);
  }
});
