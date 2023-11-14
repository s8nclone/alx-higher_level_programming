#!/usr/bin/node
const data = require('./101-data').dict;

const newDict = {};

for (const key in data) {
  if (!newDict[data[key]]) {
    newDict[data[key]] = [key];
  } else {
    newDict[data[key]].push(key);
  }
}

console.log(newDict);
