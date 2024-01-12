#!/usr/bin/node
const request = require('request');
const epNum = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(apiUrl + epNum, function (err, response, body) {
  if (!err) {
    const parsedData = JSON.parse(body);
    console.log(parsedData.title);
  }
});
