-- displays all shows WITH OR WITHOUT GENRE
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
--Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
--If a show doesn’t have a genre, display NULL
--You can use only one SELECT statement
SELECT ts.title, tg.genre_id
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tg
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id  ASC;