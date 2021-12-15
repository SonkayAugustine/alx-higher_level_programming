#!/usr/bin/node
function Factorial (n) {
  if (!n) {
    return 1;
  } else {
    return n * Factorial(n - 1);
  }
}
const args = process.argv.slice(1);
const n = parseInt(args[1]);
const fact = Factorial(n);
console.log(fact);
