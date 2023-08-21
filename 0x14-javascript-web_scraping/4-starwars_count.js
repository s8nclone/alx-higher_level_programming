#!/usr/bin/node
const request = require('request');
const argv = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films';
const xterId = '18';
let count = 0;

request.get(api + argv, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(xterId)) {
          count ++;
        }
      });
    });
    console.log(count);
  }
});
