#!/usr/bin/node

const list = require('./100-data');

console.log('Initial list:', list);

const listTwo = list.map((value, index) => value * index);

console.log('New list:', listTwo);
