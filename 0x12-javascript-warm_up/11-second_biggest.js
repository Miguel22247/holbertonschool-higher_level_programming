#!/usr/bin/node
const ArgList = [];
process.argv.forEach((val, index) => {
  ArgList[index] = `${val}`;
});
if (ArgList <= 3) {
  console.log('0');
} else {
  ArgList.sort(function (a, b) { return a - b; });
  console.log(ArgList[ArgList.length - 2]);
}
