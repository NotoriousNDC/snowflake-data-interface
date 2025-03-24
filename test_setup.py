import sys
import snowflake.connector
from dotenv import load_dotenv
import os

def test_python_version():
    print(f"Python version: {sys.version}")

def test_snowflake_import():
    print("Snowflake connector successfully imported")

def test_env_setup():
    load_dotenv()
    required_vars = ['SNOWFLAKE_ACCOUNT', 'SNOWFLAKE_USER', 'SNOWFLAKE_PASSWORD', 'SNOWFLAKE_DATABASE']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Warning: Missing environment variables: {', '.join(missing_vars)}")
    else:
        print("All required environment variables are set")

if __name__ == "__main__":
    print("Running environment tests...")
    test_python_version()
    test_snowflake_import()
    test_env_setup()
    print("Tests completed") 