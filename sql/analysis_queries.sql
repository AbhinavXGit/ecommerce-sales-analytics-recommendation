-- 1. Total revenue
SELECT SUM(revenue) AS total_revenue
FROM sales;

-- 2. Total orders
SELECT COUNT(DISTINCT order_id) AS total_orders
FROM sales;

-- 3. Average order value
SELECT
    SUM(revenue) / COUNT(DISTINCT order_id) AS average_order_value
FROM sales;

-- 4. Revenue by category
SELECT
    category,
    SUM(revenue) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC;

-- 5. Top-selling products
SELECT
    product_name,
    SUM(quantity) AS units_sold
FROM sales
GROUP BY product_name
ORDER BY units_sold DESC
LIMIT 10;

-- 6. Top customers
SELECT
    customer_name,
    SUM(revenue) AS total_spend
FROM sales
GROUP BY customer_name
ORDER BY total_spend DESC
LIMIT 10;
