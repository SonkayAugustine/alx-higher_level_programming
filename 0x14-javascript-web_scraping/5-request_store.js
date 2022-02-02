#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const store = {
  url: process.argv[2],
  method: 'GET'
};
request.get(store).on('error', function (err) {
  console.log(err);
}).pipe(fs.createWriteStream(process.argv[3]));
