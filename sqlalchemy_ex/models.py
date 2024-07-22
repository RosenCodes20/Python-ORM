from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE = ""

engine = create_engine(DATABASE)

Base = declarative_base()


Base.metadata.create_all(engine)
