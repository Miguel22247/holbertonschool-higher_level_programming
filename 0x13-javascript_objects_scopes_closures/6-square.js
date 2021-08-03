#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    const Print = 'X';
    if (!c) {
      for (let x = 0; x < this.width; x++) {
          console.log(c.repeat(this.height));
      }
    } else {
        for (let x = 0; x < this.width; x++) {
            console.log(Print.repeat(this.width))

      }
    }
  }
}
module.exports = Square;
