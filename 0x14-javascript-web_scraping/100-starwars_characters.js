#!/usr/bin/node
const request = require('request');
const argv = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + argv, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const xters = data.characters;
  for (const i of xters) {
    request.get(i, function (err, res, xbody) {
      if (err) {
        console.log(err);
      }
      const dataX = JSON.parse(xbody);
      console.log(dataX.name);
    });
  }
});
