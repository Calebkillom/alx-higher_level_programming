#!/usr/bin/node

const ogSquare = require('./5-square');

module.exports = class Square extends ogSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let a = 0; a < this.height; a++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
