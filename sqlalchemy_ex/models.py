from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE = "postgresql+psycopg://postgres:rosen12345@localhost:5432/alchemy_ex"

engine = create_engine(DATABASE)

Base = declarative_base()


Base.metadata.create_all(engine)