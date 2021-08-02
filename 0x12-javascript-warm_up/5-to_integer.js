#!/usr/bin/node
const arg = [];
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const number = Number(`${arg[2]}`);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
