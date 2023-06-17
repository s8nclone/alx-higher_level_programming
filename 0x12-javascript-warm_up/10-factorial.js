#!/usr/bin/node
const firstArgv = parseInt(process.argv[2]);
function factorial (firstArgv) {
  if (isNaN(firstArgv) || firstArgv === 1) {
    return (1);
  } else {
    return (firstArgv * factorial(firstArgv - 1));
  }
}

console.log(factorial(firstArgv));
