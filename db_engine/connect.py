from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from database_config import url_to_db
from colorama import Fore, Style, init

# Initialize colorama
init()

# Create a connection to the database
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    # Check the connection
    try:
        connection = engine.connect()
        print(Fore.GREEN + "Database connection successful!" + Style.RESET_ALL)
        connection.close()
    except Exception as e:
        print(Fore.RED + "Database connection error:" + Style.RESET_ALL, e)