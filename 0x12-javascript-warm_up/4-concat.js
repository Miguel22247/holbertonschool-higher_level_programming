#!/usr/bin/node
const arg = [];
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
console.log(`${arg[2]} is ${arg[3]}`);
