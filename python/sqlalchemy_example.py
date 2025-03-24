from sqlalchemy import create_engine
import pandas as pd

# Create SQLAlchemy engine - replace with your credentials
connection_string = (
    "snowflake://{user}:{password}@{account}/{database}/{schema}?"
    "warehouse={warehouse}&role={role}"
).format(
    user='your_username',
    password='your_password',
    account='your-account-identifier',
    database='your_database',
    schema='your_schema',
    warehouse='your_warehouse',
    role='your_role'
)

engine = create_engine(connection_string)

# Query data directly into pandas DataFrame
df = pd.read_sql("SELECT * FROM your_table_name LIMIT 100", engine)

# Display results
print(df.head())

# Perform transformations
# Example: filtering data
filtered_df = df[df['some_column'] > 100]
print(f"Filtered count: {len(filtered_df)}")

# Example: group by
grouped = df.groupby('category_column').agg({'value_column': ['mean', 'sum', 'count']})
print(grouped) 