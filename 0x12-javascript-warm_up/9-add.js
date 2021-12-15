#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const args = process.argv.slice(1);
const a = parseInt(args[1]);
const b = parseInt(args[2]);
const _add = add(a, b);
console.log(_add);
