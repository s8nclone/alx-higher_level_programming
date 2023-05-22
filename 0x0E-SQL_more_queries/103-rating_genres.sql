-- Script that lists all genres in the database hbtn_0d_tvshows_rate by their ratin
-- Records should display tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
SELECT `name`, SUM(`rate`) AS `rating`
  	FROM `tv_genres` AS genre
       	INNER JOIN `tv_show_genres` AS show
       	ON show.`genre_id` = genre.`id`
       	INNER JOIN `tv_show_ratings` AS rate
       	ON rate.`show_id` = show.`show_id`
 	GROUP BY `name`
 	ORDER BY `rating` DESC;
