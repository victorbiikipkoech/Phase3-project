# weather/db.py

from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from weather.models import Base  # Import Base from your models module

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Check if tables exist before creating them
inspector = inspect(engine)
existing_tables = inspector.get_table_names()
if not existing_tables:
    Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Uncomment the following line to define Base
Base: DeclarativeMeta = declarative_base()

def init_db():
    # Optional: Add any initialization logic here
    pass
