#!/usr/bin/node
const inputNum = process.argv[2];
console.log(inputNum);
const converted = +inputNum;
if (!converted) {
  console.log('Not a number');
} else {
  console.log(`My number: ${converted}`);
}
