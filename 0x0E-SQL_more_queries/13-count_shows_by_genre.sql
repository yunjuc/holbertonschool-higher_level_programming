-- list all genres in the database and display the numbers of shows linked
SELECT name AS genre, count(genre_id) AS number_shows FROM tv_genres RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY genre ORDER BY number_shows DESC;
