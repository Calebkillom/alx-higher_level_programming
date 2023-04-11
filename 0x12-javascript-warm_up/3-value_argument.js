#!/usr/bin/node

const process = require('process');

const val = process.argv.slice(2);
const val1 = val[0];

if (val1) {
  console.log(val1);
} else {
  console.log('No argument');
}
