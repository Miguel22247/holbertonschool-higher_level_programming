#!/usr/bin/node
const Argv1 = process.argv;
const Argv2 = process.argv;
const number1 = Number(Argv1[2]);
const number2 = Number(Argv2[3]);

function add (a, b) {
  const sum = number1 + number2;
  console.log(sum);
}

add(number1, number2);
