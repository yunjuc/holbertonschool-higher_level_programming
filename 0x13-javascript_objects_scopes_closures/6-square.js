#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
