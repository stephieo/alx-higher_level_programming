#!/usr/bin/node
$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',

    success: function (data) {
      $('#hello').text(data.hello);
    }
  });
});
