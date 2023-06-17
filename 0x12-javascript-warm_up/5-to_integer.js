#!/usr/bin/node
let firstArgv = process.argv[2];
if (!firstArgv || isNaN(firstArgv)) {
  console.log('Not a number');
} else {
  firstArgv = parseInt(firstArgv);
  console.log('My number: ' + firstArgv);
}
