-- lists all shows 
-- in the database
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id=tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;

