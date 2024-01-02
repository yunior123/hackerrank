-- # write a query to print the id, first_name, last_name. 
-- # to filter the names concatenate the first and last name to create a combined name.
-- # return the names of customers whose combined name is less than 12 characters long.
-- # order the results by the their combined names length, then alphabetically, case sensitive,by combined name, then by id.
-- # all sorts should be ascending.

-- # ex 
-- # id | first_name | last_name 
-- #  1 | Alex       | WHITE
-- #  2 | Tyler       | Hanson
-- #  3 | Riley       | Garza

-- # should return
-- # id | first_name | last_name
-- #  1 | Alex       | WHITE
-- #  3 | Riley       | Garza
-- # 2 | Tyler       | Hanson

SELECT id, first_name, last_name
FROM customer
WHERE LENGTH(CONCAT(first_name, last_name)) < 12
ORDER BY LENGTH(CONCAT(first_name, last_name)), CONCAT(first_name, last_name), id;