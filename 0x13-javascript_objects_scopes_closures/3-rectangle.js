#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (h > 0 && w > 0) {
        this.width = w;
        this.height = h;
      }
      if (!w || !h) {
        return;
      }
    }
  
  print () {
    const print = 'X';
    for (let x = 0; x < this.height; x++) {
        console.log(print.repeat(this.width));
    }
  }
};
module.exports = Rectangle;
