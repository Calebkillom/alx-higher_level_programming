#!/usr/bin/node

const process = require('process');
const argum = process.argv[2];
const numb = parseInt(argum);

if (!isNaN(numb)) {
  console.log(`My number: ${numb}`);
} else {
  console.log('Not a number');
}
