#!/usr/bin/node
const args = process.argv.slice(1);
const errMsg = 'Missing number of occurences';
const check = Number(args[1]);
if (!check) {
  console.log(errMsg);
} else {
  const c = parseInt(check);
  for (let i = 0; i < c; i++) {
    console.log('C is fun');
  }
}
