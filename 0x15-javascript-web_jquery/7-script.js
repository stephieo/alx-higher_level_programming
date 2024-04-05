#!/usr/bin/node
$(document).ready(function () {
  $.ajax({
    url: ' https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json',

    success: function (data) {
      $('#character').append('<p>' + data.name + '</p>');
    }

  });
});
