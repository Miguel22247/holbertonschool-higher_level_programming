#!/usr/bin/node
// This script prints using arguments

if (process.argv.length < 3) {
	console.log ("No arguments");
} else if (process.argv.length === 1) {
	console.log ("Argument found");
} else {
	console.log("Argument found")
}
