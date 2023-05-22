-- Script that lists all sows contained in hbtn_0d_tvsows without a genre linked
-- Record should display tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_shows LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	WHERE tv_show_genres.show_id IS NULL
	ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
