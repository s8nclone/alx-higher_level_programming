#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const myArray = process.argv.slice(2).map(Number);
  console.log(myArray.sort((a, b) => a - b)[myArray.length - 2]);
}
