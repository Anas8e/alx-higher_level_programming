#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3 || isNaN(process.argv[2])) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } else {
    console.error(`Error: Could not find a Star Wars movie with ID ${movieId}`);
  }
});
