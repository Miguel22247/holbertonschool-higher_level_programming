#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h) {
      return;
    }
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const print = 'X';
    for (let x = 0; x < this.height; x++) {
      console.log(print.repeat(this.width));
    }
  }

  rotate () {
    const temporal = this.width;
    this.width = this.height;
    this.height = temporal;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
