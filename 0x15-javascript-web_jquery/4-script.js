#!/usr/bin/node
$(document).ready(function () {
  const myHeader = $('header');
  const headerDiv = $('#toggle_header');

  // attach event handler to toggle_header

  headerDiv.on('click', function () {
    // define toggle of header
    myHeader.toggleClass('red');
    myHeader.toggleClass('green');
  });
});
