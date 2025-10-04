from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session
from dotenv import load_dotenv
import os
from os.path import join,dirname
from sqlalchemy.orm import sessionmaker


dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")


engine = create_engine(DATABASE_URL,future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
with engine.connect() as conn:
    result = conn.execute("SELECT version();")
    print(result.fetchone())