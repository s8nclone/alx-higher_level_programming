-- Script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each
-- Record should display <TV show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Results must be sorted in descending order by number of shows linked
SELECT tv_genres.name AS genre,
	COUNT(tv_show_genres.genre_id) AS number_of_shows
	FROM tv_show_genres
	INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
