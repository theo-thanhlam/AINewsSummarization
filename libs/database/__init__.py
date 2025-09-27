from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

import os

DATABASE_URL = os.getenv("DATABASE_URL")

_engine = create_engine(url=DATABASE_URL)
Session = sessionmaker(bind=_engine, expire_on_commit=False)

@contextmanager
def getSession():
    session = Session()
    session.commit()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()