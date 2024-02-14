#!/usr/bin/node
const size = process.argv[2];
const cell = 'X';
if (+size) {
  for (let i = 0; i < size; i++) {
    console.log(cell.repeat(size));
  }
} else {
  console.log('Missing size');
}
