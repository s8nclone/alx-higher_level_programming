#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/films/';
const argv = process.argv[2];

request(api + argv, function (error, response, body) {
  if (error === null) {
    const characters = JSON.parse(body).characters;
    setOrder(characters, 0);
  }
});
