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
};

module.exports = Rectangle;