from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Deck

# CRUD = Create, Read, Update, Delete

engine = create_engine(DATABASE_URI)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)