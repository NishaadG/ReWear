from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("Connected to PostgreSQL!")
    connection.close()
except Exception as e:
    print("Database connection failed:", e)
