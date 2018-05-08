#!/usr/bin/node

const list = require('./100-data.js').list;

let newList = list.map((value, i, list) => {
  return value * i;
});

console.log(list);
console.log(newList);
