#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error( error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasksByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId.toString();
      completedTasksByUser[userId] = (completedTasksByUser[userId] || 0) + 1;
    }
  });

  console.log(completedTasksByUser);
});
