#!/usr/bin/node
const request = require('request');
const argv = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/films/';

request.get(url + argv, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const dc = data.characters;
  for (const i of dc) {
    request.get(i, function (err, res, body1) {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
