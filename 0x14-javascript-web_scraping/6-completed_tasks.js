#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('API returned a non-200 status code:', response.statusCode);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      completedTasksByUser[todo.userId] = (completedTasksByUser[todo.userId] || 0) + 1;
    }
  });

  console.log(completedTasksByUser);
});
