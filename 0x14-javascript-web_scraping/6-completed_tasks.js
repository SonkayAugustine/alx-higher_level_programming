#!/usr/bin/node
// a script that computes the number of tasks completed by the user id

const request = require('request');
const arg = process.argv[2];

request(arg, function (err, response, body) {
  if (err) {
    console.log('error', err);
  } else {
    const todos = JSON.parse(body);
    const complete = {};
    for (const i = 0; i < todos.length; i++) {
      const status = (todos[i].completed);
      const key = todos[i].userId.toString();
      if (status) {
	 if (complete[key]) {
          complete[key]++;
	 } else {
          complete[key] = 1;
	 }
      }
    }
    console.log(complete);
  }
});
