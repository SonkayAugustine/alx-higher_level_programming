#!/usr/bin/node
// a script that prints the number of movies where the Character "Wedge Antilles"
// is present

const request = require('request');
const apilibrary = {
  url: process.argv[2],
  method: 'GET'
};
request(apilibrary, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    let count = 0;
    for (const item of JSON.parse(body).results) {
      for (const character of item.characters) {
	    if (character.includes(18)) {
          count++;
	    }
      }
    }
    console.log(count);
  }
});
