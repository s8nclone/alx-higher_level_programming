#!/usr/bin/node
const request = require('request');
let count = 0;

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const results = JSON.parse(body).results;
    for (let n = 0; n < results.length; n++) {
      const characters = results[n].characters;
      for (let i = 0; i < characters.length; i++) {
        if (characters[i].search('18') > 0) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
