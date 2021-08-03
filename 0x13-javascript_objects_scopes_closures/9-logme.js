#!/usr/bin/node
let LoginCounter = 0;
exports.logMe = function (item) {
  console.log(LoginCounter + ': ' + item);
  LoginCounter++;
};
