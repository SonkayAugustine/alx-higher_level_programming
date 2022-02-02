#!/usr/bin/node
// a script that prints all characters of a Star wars movie

const request = require('request');
const apilibrary = {
  url: 'https://swapi-api.hbtn.io/api/films' + process.argv[2],
  method: 'GET'
};
request(apilibrary, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    const charList = JSON.parse(body).characters;
    charList.forEach(function (element) {
	    request(element, function (error, response, body) {
        if (err) {
		    return console.log(err);
        } else {
		    console.log(JSON.parse(body).name);
        }
	    });
    });
  }
});
