from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# .env utils
DATABASE_URL = f"postgresql://postgres:root@localhost/test4"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
