#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id1 = 'https://swapi.co/api/people/18/';
const id2 = 'http://swapi.co/api/people/18/';
request(url, function (error, response, body) {
  if (error) console.log('error:', error);
  const data = JSON.parse(body);
  let count = 0;
  for (let i in data.results) {
    if (data.results[i].characters.includes(id1)||data.results[i].characters.includes(id2)) count++;
  }
  console.log(count);
});
