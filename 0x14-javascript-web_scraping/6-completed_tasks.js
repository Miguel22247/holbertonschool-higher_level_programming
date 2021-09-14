#!/usr/bin/node
const argv = process.argv;
const url = argv[2];
const request = require('request');
const dict = {};
const results = JSON.parse(body);

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (let i = 0; i < results.length; i++) {
      if (results[i].completed === true) {
        if (results[i].userId in dict) {
          dict[results[i].userId] += 1;
        } else {
          dict[results[i].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});