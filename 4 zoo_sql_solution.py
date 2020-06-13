SELECT WITHIN SELECT

#1. SELECT name FROM world WHERE population > (SELECT population FROM world WHERE name='Russia')
#2. SELECT name FROM world WHERE continent='Europe' AND (gdp/population> (SELECT gdp/population FROM world WHERE name='United Kingdom'))
#3. SELECT name, continent FROM world WHERE continent IN (SELECT continent FROM world WHERE name IN ('Argentina','Australia')) ORDER BY name
#4. SELCT name,population FROM world WHERE population > (SELECT population FROM world WHERE name='Canada') AND population <(SELECT population FROM world WHERE name='Poland')
#5. SELECT name, CONCAT(ROUND(population/(SELECT population FROM world WHERE name = 'Germany')*100), '%') FROM world WHERE continent = 'Europe'
#6. SELECT name FROM world WHERE gdp > (SELECT MAX(gdp) FROM world WHERE continent='Europe')
#7. SELECT continent, name, area FROM world x WHERE area >= ALL(SELECT area FROM world y WHERE x.continent = y.continent);
#8. SELECT continent, name FROM world x WHERE name <= ALL(SELECT name FROM world y WHERE x.continent = y.continent)
#9. SELECT name, continent, population FROM world WHERE continent IN (SELECT continent FROM world x WHERE 25000000 >= (SELECT MAX(population) FROM world y WHERE x.continent = y.continent));
#10. SELECT x.name, x.continent FROM world AS x WHERE x.population/3 > ALL SELECT y.population FROM world AS y WHERE x.continent = y.continent AND x.name != y.name);

