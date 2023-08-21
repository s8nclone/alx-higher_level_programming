#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const argv = process.argv[2];

request(api + argv, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    setCharacters(characters, 0);
  }
});

function setCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        setCharacters(characters, index + 1);
      }
    }
  });
}
