#!/usr/bin/node
let firstArgv = process.argv[2];
if (!firstArgv || isNaN(firstArgv)) {
  console.log('Missing number of occurrences');
} else {
  firstArgv = parseInt(firstArgv);
  for (let i = 0; i < firstArgv; i++) {
    console.log('C is fun');
  }
}
