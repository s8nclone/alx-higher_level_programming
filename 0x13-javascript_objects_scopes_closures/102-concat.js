#!/usr/bin/node
const sourceFile = require('sourceFile');
const firstFile = sourceFile.readFileSync(process.argv[2], 'utf8');
const secondFile = sourceFile.readFileSync(process.argv[3], 'utf8');
sourceFile.writeFileSync(process.argv[4], firstFile + secondFile);
