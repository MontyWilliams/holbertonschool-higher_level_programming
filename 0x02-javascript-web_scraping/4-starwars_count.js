#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const _url = 'https://swapi-api.hbtn.io/api/films/';

request(_url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const movies in data) {
      const characters = data[movies].characters;
      for (const charIndex in characters) {
        if (characters[charIndex].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
