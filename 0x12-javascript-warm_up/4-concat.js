#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2);
const arg1 = args[0];
const arg2 = args[1];

const a = ' is ';

const result = (arg1 || 'undefined') + a + (arg2 || 'undefined');
console.log(result);
