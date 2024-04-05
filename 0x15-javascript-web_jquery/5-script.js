#!/usr/bin/node
$(document).ready(function () {
  const triggerButton = $('#add_item');
  const listElement = $('.my_list');

  triggerButton.on('click', function () {
    listElement.append('<li>Item</li>');
  });
});
