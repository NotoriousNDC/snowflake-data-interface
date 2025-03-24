-- Snowflake Data Transformation Examples
-- These queries can be run using the Snowflake VSCode extension

-- Create a new table from query results
CREATE OR REPLACE TABLE transformed_data AS
SELECT 
  id,
  UPPER(name) AS name_upper,
  LOWER(email) AS email_lower,
  DATEADD(day, 1, date_column) AS next_day
FROM your_table_name;

-- Create a temporary table
CREATE OR REPLACE TEMPORARY TABLE temp_results AS
SELECT * FROM your_table_name
WHERE status = 'active';

-- Join tables
SELECT 
  a.id,
  a.name,
  b.description
FROM table_a a
JOIN table_b b ON a.id = b.a_id;

-- Window functions
SELECT 
  id,
  name,
  amount,
  SUM(amount) OVER (PARTITION BY customer_id) AS customer_total,
  AVG(amount) OVER (PARTITION BY customer_id) AS customer_avg,
  RANK() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS amount_rank
FROM orders;

-- Pivot data (convert rows to columns)
SELECT * 
FROM (
  SELECT product_category, amount, order_month
  FROM orders
)
PIVOT (
  SUM(amount) FOR product_category IN ('Electronics', 'Clothing', 'Food')
);

-- Unpivot data (convert columns to rows)
SELECT *
FROM products
UNPIVOT(
  price FOR size IN (small_price, medium_price, large_price)
);

-- JSON operations (if your data includes JSON)
SELECT
  id,
  JSON_EXTRACT_PATH_TEXT(json_column, 'name') AS json_name,
  JSON_EXTRACT_PATH_TEXT(json_column, 'address', 'city') AS city
FROM json_table; 