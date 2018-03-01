-- list all comedy shows in the database
SELECT title FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE genre_id =  
(SELECT id FROM tv_genres WHERE name = 'Comedy') 
ORDER BY title ASC;
