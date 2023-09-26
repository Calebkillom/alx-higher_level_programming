#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // API URL of Star Wars films
const characterId = 18; // Wedge Antilles character ID

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const filmsData = JSON.parse(body).results;
      const moviesWithWedgeAntilles = filmsData.filter((film) =>
        film.characters
          .includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
      );

      console.log(`${moviesWithWedgeAntilles.length}`);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
