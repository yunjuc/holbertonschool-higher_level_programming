-- displays the average temperature by city ordered by temperature
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state; 
