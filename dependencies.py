from models import db
from sqlalchemy.orm import sessionmaker


def pick_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()
