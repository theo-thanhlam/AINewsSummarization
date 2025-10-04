from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

_engine = create_engine(url=DATABASE_URL)
Session = sessionmaker(bind=_engine, expire_on_commit=False)

@contextmanager
def getSession():
    session = Session()
    
    try:
        yield session
        
    except:
        session.rollback()
        raise
    finally:
        session.close()