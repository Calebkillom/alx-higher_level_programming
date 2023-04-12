#!/usr/bin/node

const process = require('process');

function add(a, b) {
  let sum = a + b;
  console.log(sum);
}

const numb1 = parseInt(process.argv[2]);
const numb2 = parseInt(process.argv[3]);

add(numb1, numb2);
