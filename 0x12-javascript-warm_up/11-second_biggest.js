#!/usr/bin/node
let arg = [];
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    arg.push(process.argv[i]);
  }
  arg.sort();
  console.log(arg[arg.length - 2]);
}
