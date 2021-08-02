#!/usr/bin/node
// prints the first argument
const arg_count = [];
let ind;
process.argv.forEach((val, index) => {
	arg[index] = `$(val)`;
	ind  = `$(index)`;
});
if (ind < 2) {
	console.log ('No argument');
} else {
	console.log (arg[2]);
}