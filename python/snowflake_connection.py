import os
from dotenv import load_dotenv
import snowflake.connector
from typing import Optional

def get_snowflake_connection(config_path: Optional[str] = None):
    """
    Create a Snowflake connection using environment variables or a config file.
    
    Args:
        config_path (str, optional): Path to .env file. Defaults to None.
    
    Returns:
        snowflake.connector.SnowflakeConnection: Snowflake connection object
    """
    # Load environment variables from .env file
    if config_path:
        load_dotenv(config_path)
    else:
        load_dotenv()  # Will look for .env in current and parent directories

    # Check for key pair authentication
    private_key_path = os.getenv('PRIVATE_KEY_PATH')
    private_key_passphrase = os.getenv('PRIVATE_KEY_PASSPHRASE')
    
    connection_params = {
        'account': os.getenv('SNOWFLAKE_ACCOUNT'),
        'user': os.getenv('SNOWFLAKE_USER'),
        'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
        'database': os.getenv('SNOWFLAKE_DATABASE'),
        'schema': os.getenv('SNOWFLAKE_SCHEMA'),
        'role': os.getenv('SNOWFLAKE_ROLE'),
    }

    # Add authentication method
    if private_key_path:
        with open(private_key_path, 'rb') as key:
            p_key = key.read()
        connection_params['private_key'] = p_key
        if private_key_passphrase:
            connection_params['private_key_passphrase'] = private_key_passphrase
    else:
        connection_params['password'] = os.getenv('SNOWFLAKE_PASSWORD')

    # Add optional parameters if they exist
    if os.getenv('SNOWFLAKE_REGION'):
        connection_params['region'] = os.getenv('SNOWFLAKE_REGION')
    
    if os.getenv('SNOWFLAKE_SESSION_PARAMETERS'):
        connection_params['session_parameters'] = os.getenv('SNOWFLAKE_SESSION_PARAMETERS')

    # Create and return connection
    return snowflake.connector.connect(**connection_params)

def test_connection():
    """Test the Snowflake connection using current environment variables."""
    try:
        conn = get_snowflake_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT current_version()')
        version = cursor.fetchone()[0]
        print(f"Successfully connected to Snowflake! Version: {version}")
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Failed to connect to Snowflake: {str(e)}")
        return False

if __name__ == '__main__':
    test_connection() 