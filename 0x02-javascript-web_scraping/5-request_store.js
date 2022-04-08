#!/usr/bin/node

const fileServer = require('fs');
const request = require('request');
const _url = process.argv[2];
const file = process.argv[3];
request(_url).pipe(fileServer.createWriteStream(file));
