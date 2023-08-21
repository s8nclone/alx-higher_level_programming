#!/usr/bin/node
const request = require('request');
const argv = process.argv[2];
const xterId = '18';
let count = 0;

request.get(argv, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(xterId)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
