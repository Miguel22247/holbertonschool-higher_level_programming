-- lists only comedy genre
-- of the database
SELECT tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id=tv_shows.id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genre.name = 'Comedy'
ORDER BY tv_shows.title;