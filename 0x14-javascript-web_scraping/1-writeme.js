#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const str = process.argv[2];

fs.writeFile(args, str, 'utf-8', (error) => {
	if (error) {
		console.log(error);
	}
});

