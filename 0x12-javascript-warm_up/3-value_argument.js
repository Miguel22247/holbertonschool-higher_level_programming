#!/usr/bin/node
// prints the first argument
const ArgCount = [];
let ind;
process.argv.forEach((val, index) => {
  ArgCount[index] = `${val}`;
  ind = `${index}`;
});
if (ind < 2) {
  console.log('No argument');
} else {
  console.log(ArgCount[2]);
}
