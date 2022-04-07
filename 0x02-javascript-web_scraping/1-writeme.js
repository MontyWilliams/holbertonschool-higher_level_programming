#!/usr/bin/node

const _request = require('fs');
const file = process.argv[2];
const text = process.argv[3];
_request.writeFile(file, text, 'utf-8', function (error, content) {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
