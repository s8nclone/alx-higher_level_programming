-- Script that lists all shows and all genres linked to that show
-- Display NULL in the genre column if show doesn't have a genre
-- Record should display tv_shows.title - tv_genres.name
-- Results must be sorted in ascending aorder by the show title and genre name
SELECT tv_shows.title, tv_genres.name
       FROM tv_shows
       LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
       LEFT JOIN tv_genres
       ON tv_genres.id = tv_show_genres.genre_id
       ORDER BY tv_shows.title ASC, tv_genres.name ASC;
