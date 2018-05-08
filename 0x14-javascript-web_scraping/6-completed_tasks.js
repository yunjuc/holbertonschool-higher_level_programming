#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log('error:', error);
  const data = JSON.parse(body);
  let dict = {};
  for (let i in data) {
    if (data[i].completed) {
      let id = data[i].userId;
      if (dict[id]) {
        dict[id]++;
      } else {
        dict[id] = 1;
      }
    }
  }
  console.log(dict);
});
