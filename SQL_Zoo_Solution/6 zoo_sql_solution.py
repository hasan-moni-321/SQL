More JOIN operations


#1. SELECT id,title FROM movie WHERE yr=1962
#2. SELECT yr FROM movie WHERE title='Citizen Kane'
#3. SELECT id,title,yr FROM movie WHERE title LIKE ('%Star Trek%') ORDER BY yr
#4. SELECT id FROM actor WHERE name= 'Glenn Close'
#5. SELECT id FROM movie WHERE title='Casablanca'
#6. SELECT name FROM actor JOIN casting ON (actor.id=casting.actorid) WHERE casting.movieid = 11768
#7. SELECT actor.name FROM actor JOIN casting ON casting.actorid = actor.id JOIN movie ON movie.id = casting.movieid WHERE movie.title = 'Alien'
#8. SELECT movie.title FROM movie JOIN casting ON casting.movieid = movie.id JOIN actor ON actor.id = casting.actorid WHERE actor.name ='Harrison Ford'
#9. SELECT movie.title FROM movie JOIN casting ON (movie.id=casting.movieid) JOIN actor ON (actor.id=casting.actorid) WHERE actor.name='Harrison Ford' AND casting.ord !=1
#10. SELECT movie.title, actor.name FROM movie JOIN casting ON (movie.id=casting.movieid) JOIN actor ON (actor.id=casting.actorid) WHERE movie.yr=1962 AND casting.ord=1
#11. SELECT yr,COUNT(title) FROM movie JOIN casting ON movie.id=movieid JOIN actor ON actorid=actor.id WHERE name='Rock Hudson' GROUP BY yr HAVING COUNT(title) > 2
#12. SELECT DISTINCT m.title, a.name FROM (SELECT movie.* FROM movie JOIN casting ON casting.movieid=movie.id JOIN actor ON actor.id = casting.actorid WHERE actor.name=’Julie Andrews’) AS m JOIN(SELECT actor.*, casting.movieid AS movieid FROM actor JOIN casting ON casting.actorid=actor.id WHERE casting.ord=1) as a ON m.id=a.movieid ORDER BY m.title;
#13. SELECT actor.name FROM actor JOIN casting ON casting.actorid = actor.id WHERE casting.ord=1 GROUP BY actor.name HAVING COUNT(*) >= 15 ORDER BY actor.name
#14.
#15.


