#!/usr/bin/node
const data = require('./100-data').list;

const newList = data.map((item, index) => item * index);

console.log(data);
console.log(newList);
