-- For each contry display the contry name, total number of invoi es, and their average amount
-- format the average as a floating point number with 6 decimal places
-- return only countries where their average invoice amount is greater than the overall inv oice amount
-- over all invoices.

country 

# id | country_name
# 1 | USA

city
# id | city_name | country_id

customer
# id | customer_name | city_id

invoice
# id | customer_id | total

SELECT country.country_name, COUNT(invoice.id) AS total_invoices, ROUND(AVG(invoice.total), 6) AS average_invoice
FROM country
JOIN city ON city.country_id = country.id
JOIN customer ON customer.city_id = city.id
JOIN invoice ON invoice.customer_id = customer.id
GROUP BY country.country_name
HAVING ROUND(AVG(invoice.total), 6) > (SELECT AVG(total) FROM invoice)
ORDER BY average_invoice DESC;