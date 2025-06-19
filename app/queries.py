# queries.py

REVENUE_BY_MONTH = """
SELECT 
    DATE(payment_date) AS date,
    ROUND(SUM(amount)::numeric, 2) AS revenue
FROM payments
GROUP BY DATE(payment_date)
ORDER BY DATE(payment_date);
"""

TOP_CUSTOMERS = """
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    ROUND(SUM(p.amount)::numeric, 2) AS total_spent
FROM payments p
JOIN customers c ON p.customer_id = c.customer_id
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 10;
"""

POPULAR_GENRES = """
SELECT 
    g.genre_name AS genre,
    COUNT(*) AS rentals
FROM rentals r
JOIN films f ON r.film_id = f.film_id
JOIN genres g ON f.genre_id = g.genre_id
GROUP BY g.genre_name
ORDER BY rentals DESC;
"""

TOTAL_REVENUE = """
SELECT ROUND(SUM(amount)::numeric, 2) AS total_revenue FROM payments;
"""

TOTAL_RENTALS = """
SELECT COUNT(*) AS total_rentals FROM rentals;
"""

TOTAL_CUSTOMERS = """
SELECT COUNT(*) AS total_customers FROM customers WHERE active = 1;
"""
