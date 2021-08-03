#!/usr/bin/node
const Squeare5 = require('./5-square');

class Square extends Squeare5 {
  charPrint (c) {
    const Print = 'X';
    if (!c) {
      for (let x = 0; x < this.width; x++) {
        console.log(Print.repeat(this.height));
      }
    } else {
      for (let y = 0; y < this.width; y++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
