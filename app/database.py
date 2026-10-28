import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

db_url = URL.create(
    drivername="postgresql+psycopg", 
    host = os.getenv("DB_HOST"),
    port =int(os.getenv("DB_PORT")),
    database = os.getenv("DB_NAME"),
    username = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
)

engine = create_engine(db_url)
if __name__ == "__main__":
    with engine.connect():
        print("SQLalchemy connected!")
