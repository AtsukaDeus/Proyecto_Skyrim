$(document).ready(function() {
   
    $("#get-joke-button").click(function() {
     
        $.getJSON("https://api.chucknorris.io/jokes/random", function(data) {
        $("#joke-text").text(data.value);
     

    });
    });
  });
  