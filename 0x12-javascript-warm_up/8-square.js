#!/usr/bin/node

const process = require('process');
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    let element = '';
    for (let column = 0; column < size; column++) {
      element += 'X';
    }
    console.log(element);
  }
}
