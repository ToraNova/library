#!/usr/bin/node

/*
 * This script is used to generate a random JWT key
 * the key can then be used to sign JWT generated
 */

//requires the filesystem module and crypto (for random byte gen)
const fs = require('fs');
const crypto = require('crypto');

//gen random key and cast it to hex
var token = crypto.randomBytes(128).toString('hex');
token = `exports.secret = \"${token}\"`;

//write to file
fs.writeFile("./.jwt", token, function(err) {
	if(err) {
		return console.log(err);
	}
	console.log("JWT Key Initialized.");
});

