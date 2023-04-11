#!/usr/bin/node

const process = require('process');

const numb = parseInt(process.argv[2]);

if (isNaN(numb)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < numb) {
    console.log('C is fun');
    i++;
  }
}
