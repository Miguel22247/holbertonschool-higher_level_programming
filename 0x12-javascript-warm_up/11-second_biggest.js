#!/usr/bin/node
const arg = process.argv;
const ArgList = [];
arg.forEach((val, index) => {
  ArgList[index] = `${val}`;
});
if (ArgList.length <= 3) {
  console.log('0');
} else {
  ArgList.sort(function (a, b) { return a - b; });
  console.log(ArgList[ArgList.length - 2]);
}
