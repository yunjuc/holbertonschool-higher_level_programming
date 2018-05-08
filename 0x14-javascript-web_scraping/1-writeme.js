#!/usr/bin/node

let fs = require('fs');
let file = process.argv[2];
let message = process.argv[3];
fs.writeFile(file, message, function (err, data) {
  if (err) {
    return console.log(err);
  }
});
