#!/usr/bin/node
let firstArgv = process.argv[2];
if (!firstArgv || isNaN(firstArgv)) {
  console.log('Missing size');
} else {
  firstArgv = parseInt(firstArgv);
  for (let i = 0; i < firstArgv; i++) {
    console.log('X'.repeat(firstArgv));
  }
}
