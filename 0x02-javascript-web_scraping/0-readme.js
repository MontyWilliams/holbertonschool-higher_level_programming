#!/usr/bin/node

const _request = require('fs');
const file = process.argv[2];
_request.readFile(file, 'utf-8', function (error, content) {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
