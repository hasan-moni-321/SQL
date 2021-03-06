SUM and COUNT

#1. SELECT SUM(population) FROM world
#2. select DISTINCT continent from world
#3. SELECT SUM(gdp) FROM world WHERE continent='Africa'
#4. SELECT COUNT(name) FROM world WHERE area>=1000000
#5. SELECT SUM(population) FROM world WHERE name IN ('Estonia', 'Latvia', 'Lithuania')
#6. SELECT continent, COUNT(name) FROM world GROUP BY continent
#7. SELECT continent, COUNT(name) FROM world WHERE population >=10000000 GROUP BY continent
#8. SELECT continent FROM world GROUP BY continent HAVING SUM(population) >=100000000 JOIN
#1. SELECT matchid,player FROM goal WHERE teamid='GER'
#2. SELECT id,stadium,team1,team2 FROM game WHERE id=1012
#3. SELECT player,teamid,stadium,mdate FROM game JOIN goal ON (id=matchid) where teamid='GER'
#4. SELECT team1,team2,player FROM game JOIN goal ON (id=matchid) WHERE player LIKE 'Mario%'
#5. SELECT player,teamid,coach,gtime FROM goal JOIN eteam ON (teamid=id) WHERE gtime<=10
#6. SELECT mdate, teamname FROM game JOIN eteam ON (game.team1=eteam.id) WHERE coach='Fernando Santos'
#7. SELECT player FROM goal JOIN game ON (goal.matchid=game.id) WHERE stadium='National Stadium, Warsaw'
#8. SELECT DISTINCT player FROM game JOIN goal ON goal.matchid = game.id WHERE (team1 = 'GER' OR team2 = 'GER') AND teamid <> 'GER'
#9. SELECT teamname, COUNT(player) FROM eteam JOIN goal ON (goal.teamid=eteam.id) GROUP BY teamname
#10. SELECT stadium, COUNT(player) FROM game JOIN goal ON (game.id=goal.matchid) GROUP BY stadium
#11. SELECT matchid, mdate, COUNT(player) FROM goal JOIN game ON (goal.matchid=game.id) WHERE (team1='POL' OR team2='POL') GROUP BY goal.matchid
#12. SELECT matchid, mdate, COUNT(player) FROM game JOIN goal ON (game.id=goal.matchid) WHERE teamid='GER' GROUP BY matchid
#13. SELECT mdate, team1, SUM(CASE WHEN teamid = team1 THEN 1 ELSE 0 END) AS score1, team2, SUM(CASE WHEN teamid = team2 THEN 1 ELSE 0 END) AS score2 FROM game LEFT JOIN goal ON (id = matchid) GROUP BY mdate,team1,team2 ORDER BY mdate, matchid, team1, team2

