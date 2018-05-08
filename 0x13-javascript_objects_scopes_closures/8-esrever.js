#!/usr/bin/node

exports.esrever = function (list) {
  let reverse = [];
  let length = list.length;
  for (let i = length - 1; i >= 0; i--) {
    reverse.push(list[i]);
  }
  return reverse;
};
