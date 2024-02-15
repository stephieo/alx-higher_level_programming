#!/usr/bin/node
const number = process.argv[2];

function factorial (number) {
  if (!number || number === 1) {
    return 1;
  } else {
    return (factorial(number - 1) * number);
  }
}

console.log(factorial(number));
