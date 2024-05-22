#!/usr/bin/node

exports.esrever = function (lst) {
  const len = lst.length;
  const revlst = [];
  for (let ptr = len - 1; ptr > -1; ptr--) {
    revlst.push(lst[ptr]);
  }
  return revlst;
};
