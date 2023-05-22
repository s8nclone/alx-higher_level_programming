-- Script that lists all shows contained in hbtn_0d_tvshows
-- that have at least on genre linked
-- Record should display tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_shows INNER JOIN yv_show_enres
	ON tv_shows.id = tv_show_genres.show_id
	ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
