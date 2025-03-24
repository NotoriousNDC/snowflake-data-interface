-- Snowflake Data Exploration Examples
-- These queries can be run using the Snowflake VSCode extension

-- List all databases
SHOW DATABASES;

-- List schemas in the current database
SHOW SCHEMAS;

-- List tables in the current schema
SHOW TABLES;

-- Get table metadata 
DESCRIBE TABLE your_table_name;

-- Sample data exploration
SELECT * 
FROM your_table_name
LIMIT 100;

-- Get column statistics
SELECT 
  column_name,
  COUNT(*) as row_count,
  COUNT(DISTINCT column_name) as distinct_count,
  AVG(column_name) as avg_value,
  MIN(column_name) as min_value,
  MAX(column_name) as max_value
FROM your_table_name
GROUP BY column_name;

-- Find null values in a table
SELECT 
  column_name, 
  COUNT(*) as null_count
FROM your_table_name
WHERE column_name IS NULL
GROUP BY column_name;

-- Time-based analysis (example)
SELECT 
  DATE_TRUNC('month', date_column) as month,
  COUNT(*) as event_count
FROM your_table_name
GROUP BY DATE_TRUNC('month', date_column)
ORDER BY month; 