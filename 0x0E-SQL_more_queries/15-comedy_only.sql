-- Script that lists all comedy shows in the database hbtn_0d_tvshows
--The tv_genres tale contains only one record where name = Comedy
-- Record must display tv_shows.title
-- Records must be sorted in ascending order by the show title
SELECT tv_shows.title As titles
	FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_show_genres.show_id = tv_shows.id
	INNER JOIN tv_genres
	ON tv_genres.id = tv_show_genres.genre_id
	AND tv_genres.name = 'Comedy'
	ORDER BY titles;
