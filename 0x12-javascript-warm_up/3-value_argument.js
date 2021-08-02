#!/usr/bin/node
// prints the first argument
const arg_count = [];
let ind;
process.argv.forEach((val, index) => {
	arg_count[index] = `$(val)`;
	ind  = `$(index)`;
});
if (ind < 2) {
	console.log ('No argument');
} else {
	console.log (arg_count[2]);
}