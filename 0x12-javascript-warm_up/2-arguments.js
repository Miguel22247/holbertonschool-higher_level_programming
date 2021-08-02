#!/usr/bin/node
// This script prints using arguments
const argv_length = process.argv.length;

if (argv_length < 3) {
  console.log('No arguments');
} else if (argv_length === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
