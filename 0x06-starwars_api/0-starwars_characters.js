#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Enter movie ID');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

const fetchMovie = (url) => {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        const movie = JSON.parse(body);
        resolve(movie);
      }
    });
  });
};

const fetchCharacters = (movie) => {
  return Promise.all(
    movie.characters.map(async (characterUrl) => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    })
  );
};

const main = async () => {
  try {
    const movie = await fetchMovie(apiUrl);
    const characters = await fetchCharacters(movie);

    characters.forEach((actor) => console.log(actor));
  } catch (err) {
    console.log(err);
  }
};

main();
