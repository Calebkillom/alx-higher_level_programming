#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('API returned a non-200 status code:', response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  if (!characterUrls || characterUrls.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  // Function to fetch and print character names in order
  function printNextCharacterName (index) {
    if (index < characterUrls.length) {
      request(characterUrls[index], (err, res, characterBody) => {
        if (err) {
          console.error('Error:', err);
        } else if (res.statusCode === 200) {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);

          // Fetch and print the next character
          printNextCharacterName(index + 1);
        }
      });
    }
  }

  // Start fetching and printing characters from the first character URL
  printNextCharacterName(0);
});
