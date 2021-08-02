#!/usr/bin/node
// if not argmuents console.log ("No arguments")
// else if argmuents == 1 then console.log ("Argument found")
//else console.log ("Argument found")

if (process.argv.length < 3) {
	console.log ("No arguments");
} else 
if (process.argv.length === 1) {
	console.log ("Argument found");
} else {
	console.log("Argument found")
}