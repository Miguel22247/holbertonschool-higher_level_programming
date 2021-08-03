#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
      if (h > 0 && w > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
  print () {
    const print = 'X';
    let x;
    for (x = 0; x < this.height; x++) {
        console.log(print.repeat(this.width));
    }
  }
};
