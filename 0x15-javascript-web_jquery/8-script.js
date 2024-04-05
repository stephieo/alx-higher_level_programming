#!/usr/bin/node
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',

    success: function (data) {
      const movies = data.results;
      $.each(movies, function (movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    }

  });
});
