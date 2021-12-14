#!/usr/bin/node
const arg = process.argv.slice(1);
if (arg[1]) {
  console.log(arg[1]);
} else {
  console.log('No argument');
}
