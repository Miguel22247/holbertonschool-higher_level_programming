#!/usr/bin/node
const arg = [];
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
console.log(factorial(arg[2]));
