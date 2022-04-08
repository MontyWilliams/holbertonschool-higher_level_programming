#!/usr/bin/node

const request = require('request');
const _url = process.argv[2];
request(_url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const task = {};
    const content = JSON.parse(body);
    for (let i = 0; i < content.length; i++) {
      const id = content[i].userId;
      const completed = content[i].completed;
      if (completed) {
        if (!task[id]) {
          task[content[i].userId] = 1;
        } else {
          task[content[i].userId] += 1;
        }
      }
    }
    console.log(task);
  }
});
