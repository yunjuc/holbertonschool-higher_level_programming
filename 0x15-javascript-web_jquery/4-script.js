$('#toggle_header').on('click', function() {
  if ($('header').hasClass('red')) $('header').attr('class', 'green');
  else $('header').attr('class', 'red'); 
});
