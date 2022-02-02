#!/usr/bin/node
//a script that prints the title of StarWars and given integer matches
//episode number

const request = require("request");
const apilibrary = {
    url: "https://swapi-api.hbtn.io/api/films/" + process.argv[2],
    method: "GET"
};
request(apilibrary, function (err, response, body) {
    if (err) {
	return console.log(err);
    }
    console.log(JSON.parse(body).title);
});
