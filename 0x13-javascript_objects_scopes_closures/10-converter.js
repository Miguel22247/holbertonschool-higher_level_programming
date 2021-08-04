#!/usr/bin/node
exports.converter = function (base) {
  function converted (number) {
	return number.toString(base);
  }
  return (converted);
};