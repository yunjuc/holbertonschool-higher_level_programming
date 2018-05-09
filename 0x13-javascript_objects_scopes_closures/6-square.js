#!/usr/bin/node

const Square = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        for (let j = 0; j < this.size; j++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
}

module.exports = Square;
