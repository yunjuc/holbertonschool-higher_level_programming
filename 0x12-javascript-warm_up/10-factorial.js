#!/usr/bin/node
let factorial = (n) => {
  if (n === 0 || isNaN(n) || n === undefined) return 1;
  return n * factorial(n - 1);
};
console.log(factorial(process.argv[2]));
