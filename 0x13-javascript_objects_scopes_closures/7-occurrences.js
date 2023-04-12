#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      count++;
    }
  }
  return count;
};
