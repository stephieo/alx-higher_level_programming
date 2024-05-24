#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/${id}', (error, code, body) => {
	if (error){
		console.log(error);
	} else {
		console.log(JSON.parse(body).title);
	}
});



