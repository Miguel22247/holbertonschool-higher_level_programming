#!/usr/bin/node
exports.esrever = function (list) {
  const NewList = [];
  while (list.length) {
    NewList.push(list.pop());
  }
  return (NewList);
};
