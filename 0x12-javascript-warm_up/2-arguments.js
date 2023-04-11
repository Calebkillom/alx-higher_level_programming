#!/usr/bin/node

const process = require('process');
const argue = process.argv;

if (argue.length === 2) {
  console.log('No argument');
} else if (argue.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
