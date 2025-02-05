from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database configuration dictionary
DATABASE_CONFIG = {
    'DB_NAME': os.getenv('DB_NAME'),
    'DB_USER': os.getenv('DB_USER'),
    'DB_PASSWORD': os.getenv('DB_PASSWORD'),
    'DB_HOST': os.getenv('DB_HOST'),
    'DB_PORT': os.getenv('DB_PORT'),
}

# Construct the database URL
url_to_db = f"postgresql://{DATABASE_CONFIG['DB_USER']}:{DATABASE_CONFIG['DB_PASSWORD']}@{DATABASE_CONFIG['DB_HOST']}:{DATABASE_CONFIG['DB_PORT']}/{DATABASE_CONFIG['DB_NAME']}"