-- list all genres of the show Dexter
SELECT name FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id  WHERE show_id =
(SELECT id FROM tv_shows where title = 'Dexter') 
ORDER BY name ASC;
