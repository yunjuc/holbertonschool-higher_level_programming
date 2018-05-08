#!/usr/bin/node

let request = require('request');
let fs = require('fs');
let url = process.argv[2];
let path = process.argv[3];

request
  .get(url)
  .on('error', function (err) {
    console.log(err);
  })
  .pipe(fs.createWriteStream(path));
