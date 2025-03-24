# Snowflake Data Interface

A repository for interfacing with Snowflake data using the Snowflake VSCode extension.

## Setup

1. Install the [Snowflake VSCode Extension](https://marketplace.visualstudio.com/items?itemName=snowflake.snowflake-vsc)
2. Configure your Snowflake connection in VSCode
3. Use the SQL files in this repository to query and manipulate your Snowflake data

## Project Structure

- `/sql` - SQL queries and scripts for Snowflake
- `/config` - Configuration files for Snowflake connections
- `/python` - Python scripts for Snowflake data operations

## Requirements

- Visual Studio Code or Cursor IDE
- Snowflake VSCode Extension
- Snowflake account with appropriate access
- Python 3.8+ (for Python integration)

## SQL Tutorial for Snowflake in VSCode/Cursor

### Initial Setup

1. **Install Snowflake VSCode Extension**:
   - Open VSCode/Cursor
   - Go to Extensions (or press `Ctrl+Shift+X`)
   - Search for "Snowflake"
   - Install the "Snowflake" extension by Snowflake Inc.

2. **Configure Snowflake Connection**:
   - Copy `.vscode/settings.json.example` to `.vscode/settings.json`
   - Update the settings with your Snowflake credentials:
     ```json
     "snowflake.connections": {
       "default": {
         "account": "your-account-identifier",
         "username": "your_username",
         "authenticator": "snowflake",
         "warehouse": "your_warehouse",
         "database": "your_database",
         "schema": "your_schema",
         "role": "your_role"
       }
     }
     ```

### Running SQL Queries

1. **Open an SQL file** from the `/sql` directory or create a new one
2. **Connect to Snowflake**:
   - Click on the Snowflake icon in the sidebar
   - Select your connection from the dropdown
   - Click "Connect"
3. **Execute Queries**:
   - To run the entire file: Right-click in the editor and select "Execute All"
   - To run a specific query: Select the query, right-click, and select "Execute Selected"
   - The results will appear in a new tab

### Exploring Data with Example Queries

The repository includes example queries in the `/sql` directory:
- `sample_query.sql` - Basic queries and table creation
- `data_exploration.sql` - Queries for exploring and analyzing data
- `data_transformations.sql` - Advanced data transformation examples

## Python Tutorial for Snowflake Integration

### Required Packages

Install the following Python packages:

```bash
pip install snowflake-connector-python snowflake-sqlalchemy pandas numpy matplotlib
```

### Setting Up a Python Environment

1. **Create a Virtual Environment** (recommended):
   ```bash
   # Create a virtual environment
   python -m venv snowflake-env
   
   # Activate on Windows
   snowflake-env\Scripts\activate
   
   # Activate on macOS/Linux
   source snowflake-env/bin/activate
   ```

2. **Create a Python Connection File**:
   Create a new file `python/connection.py`:

   ```python
   import snowflake.connector
   from cryptography.hazmat.backends import default_backend
   
   def get_connection(config_path=None):
       """
       Establish a connection to Snowflake.
       If config_path is provided, it will read credentials from a JSON file.
       Otherwise, it uses the credentials provided below.
       """
       if config_path:
           import json
           with open(config_path, 'r') as f:
               config = json.load(f)
               
           conn = snowflake.connector.connect(
               user=config['username'],
               password=config['password'],
               account=config['account'],
               warehouse=config['warehouse'],
               database=config['database'],
               schema=config['schema'],
               role=config['role']
           )
       else:
           # Replace with your credentials
           conn = snowflake.connector.connect(
               user='your_username',
               password='your_password',
               account='your-account-identifier',
               warehouse='your_warehouse',
               database='your_database',
               schema='your_schema',
               role='your_role'
           )
       
       return conn
   ```

### Example Python Scripts

Create a sample script `python/basic_query.py`:

```python
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
```

### Using SQLAlchemy with Snowflake

Create another example `python/sqlalchemy_example.py`:

```python
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
```

## Additional Configuration

### Authentication Options

Snowflake supports several authentication methods:

1. **Username/Password** (as shown above)
2. **Single Sign-On (SSO)**:
   ```json
   "authenticator": "externalbrowser"
   ```
3. **Key Pair Authentication**:
   ```json
   "private_key_file": "/path/to/private/key.p8",
   "private_key_passphrase": "your-passphrase"
   ```

### Troubleshooting

Common issues and solutions:

1. **Connection Issues**:
   - Verify your account identifier (includes region and cloud provider)
   - Check your network connection and firewall settings
   - Ensure your credentials are correct

2. **Query Performance**:
   - Verify your warehouse is running and properly sized
   - Use EXPLAIN to analyze query performance
   - Consider query optimization techniques

3. **Python Connectivity**:
   - Ensure you've installed all required dependencies
   - Check for version compatibility between packages
   - Use virtual environments to isolate dependencies 