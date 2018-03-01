-- list all shows and all genres linked to the shows
SELECT title, name FROM tv_show_genres
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id 
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name;
