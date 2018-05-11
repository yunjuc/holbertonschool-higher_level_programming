$.get( "https://swapi.co/api/films/?format=json", function (data) {
  let movies = data.results;
  for (let i in movies) {
    $('ul#list_movies').append('<li>' + movies[i].title + '</li>');
  }
});
