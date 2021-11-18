-- script that displays the top 3 cities temp during July-August ordered by temp(descending)
USE hbtn_0c_0;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7 OR  month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
