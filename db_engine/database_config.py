DB_USER = "postgres_user" 
DB_PASSWORD = "postgres_password"  
DB_HOST = "localhost" 
DB_PORT = "5432"  
DB_NAME = "university_db" 

# SQLAlchemy connection URL
url_to_db = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
