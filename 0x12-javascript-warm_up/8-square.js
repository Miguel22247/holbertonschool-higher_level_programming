#!/usr/bin/node
const arg = [];
const { argv } = require('process');
let x;
let square = 'X';
argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const number = Number(`${arg[2]}`);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (x = 0; x < number; x++){
  console.log(square.repeat(number));
  }
}
