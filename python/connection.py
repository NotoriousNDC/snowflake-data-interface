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