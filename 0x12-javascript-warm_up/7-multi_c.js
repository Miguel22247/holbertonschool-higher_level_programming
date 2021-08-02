#!/usr/bin/node
let i;
const arg = [];
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const number = Number(`${arg[2]}`);
if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
