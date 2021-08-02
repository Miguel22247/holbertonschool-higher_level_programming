#!/usr/bin/node
const argv = require('process');
const Number1 = Number(argv[2]);
const Number2 = Number(argv[3]);

function add (a, b) {
  const suma = Number1 + Number2;
  console.log(suma);
}
add(Number1, Number2);
