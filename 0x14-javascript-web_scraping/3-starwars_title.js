#!/usr/bin/node
const request = require('request');
const epNum = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/:id';

request(apiUrl + epNum, function (err, response, body) {
  if (err == null) {
    const parsed = JSON.parse(body);
    console.log(parsed.title);
  }
});
