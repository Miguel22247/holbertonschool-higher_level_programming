#!/usr/bin/node
// This script prints using arguments
const ArgvLength = process.argv.length;

if (ArgvLength < 3) {
  console.log('No argument');
} else if (ArgvLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
