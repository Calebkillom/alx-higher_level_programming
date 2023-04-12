#!/usr/bin/node

const process = require('process');

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

function computeFactorial (num) {
  let result;
  if (isNaN(num)) {
    result = 1;
  } else {
    result = factorial(num);
  }
  return result;
}

const input = process.argv[2];
const num = parseInt(input);

const result = computeFactorial(num);

console.log(result);
