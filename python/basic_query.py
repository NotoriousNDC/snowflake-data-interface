import pandas as pd
from connection import get_connection

# Establish connection
conn = get_connection()

# Execute a query
query = "SELECT * FROM your_table_name LIMIT 100"
cursor = conn.cursor()
try:
    cursor.execute(query)
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])
    
    # Display results
    print(f"Retrieved {len(df)} rows")
    print(df.head())
    
    # Basic analysis
    print("\nSummary Statistics:")
    print(df.describe())
    
finally:
    cursor.close()
    conn.close() 