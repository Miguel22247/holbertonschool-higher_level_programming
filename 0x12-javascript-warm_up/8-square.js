#!/usr/bin/node
const arg = [];
let x;
let square = 'X';
argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const number = Number(`${arg[2]}`);
if (isNaN(number)) {
	console.log('Missing size');
} else {
	console.log(square.repeat(number));
}
