#!/usr/bin/node
const args = process.argv.slice(1);
const errMsg = 'Missing size';
const check = Number(args[1]);
let square = '';

if (!check) {
  console.log(errMsg);
} else {
  const c = parseInt(check);
  for (let i = 0; i < c; i++) {
    for (let j = 0; j < c; j++) {
      square += 'X';
    }
    square += '\n';
  }
  square = square.slice(0, -1);
  console.log(square);
}
