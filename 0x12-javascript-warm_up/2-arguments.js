#!/usr/bin/node
const args = process.argv.slice(1);
const l = args.length;
const argsRet = ['No argument', 'Argument found', 'Arguments found'];
if (l === 1) {
  console.log(argsRet[0]);
} else if (l === 2) {
  console.log(argsRet[1]);
} else {
  console.log(argsRet[2]);
}
