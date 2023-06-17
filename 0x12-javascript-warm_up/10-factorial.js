#!/usr/bin/node
const firstArgv = parseInt(process.argv[2]);
function factorial (firstArgv) {
  if (isNaN(firstArgv) || firstArgv === 1) {
    console.log(1);
  } else {
    console.log(firstArgv * factorial(firstArgv - 1));
  }
}

factorial(firstArgv);
