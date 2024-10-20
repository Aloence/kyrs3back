from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,declarative_base

# Замените эти значения на ваши данные для подключения к PostgreSQL
DATABASE_URL = f"postgresql://postgres:root@localhost/test3"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
