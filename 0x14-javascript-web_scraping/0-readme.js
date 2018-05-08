#!/usr/bin/node

let fs = require('fs');

fs.open (process.argv[2], 'r', function (err, file) {
  if (err) {
    return console.error(err);
  }
  fs.readFile(file, 'utf8', function(err, data){
    if (err) {
      console.log(err);
    }
    console.log(data);
  });
});
