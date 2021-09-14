#!/usr/bin/node
const argu = process.argv;
const fs = require('fs');
const request = require('request');

request(argu[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(argu[3], body, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});