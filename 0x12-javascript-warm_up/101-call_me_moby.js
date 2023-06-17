#!/usr/bin/node
exports.mobyFunc = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
