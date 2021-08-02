#!/usr/bin/node
const arg = [];
const { argv } = require('process');
const square = 'X';
let x;
argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const number = Number(`${arg[2]}`);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (x = 0; x < number; x++) {
    console.log(square.repeat(number));
  }
}
