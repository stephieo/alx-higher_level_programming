#!/usr/bin/node
$(document).ready(function () {
  const triggerButton = $('#update_header');
  const myHeader = $('header');

  triggerButton.on('click', function () {
    myHeader.text('New Text');
  });
});
