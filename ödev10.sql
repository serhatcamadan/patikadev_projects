--1

SELECT country.country, city.city FROM city
LEFT JOIN country ON country.country_id = city.country_id
ORDER BY country ASC;

--2

SELECT payment_id,customer.first_name,customer.last_name FROM payment
RIGHT JOIN customer ON customer.customer_id = payment.customer_id;

--3

SELECT rental.rental_id, customer.first_name,customer.last_name FROM rental
FULL JOIN customer ON customer.customer_id = rental.customer_id