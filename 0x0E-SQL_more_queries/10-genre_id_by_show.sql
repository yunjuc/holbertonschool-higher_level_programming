-- all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, genre_id FROM tv_shows RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id WHERE genre_id >= 1 ORDER BY title, genre_id ASC;
