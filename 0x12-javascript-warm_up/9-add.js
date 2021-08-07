#!/usr/bin/node
const Argv1 = process.argv[2];
const Argv2 = process.argv[3];
const number1 = Number(Argv1);
const number2 = Number(Argv2);

function add (a, b) {
  const sum = number1 + number2;
  console.log(sum);
}

add(number1, number2);
