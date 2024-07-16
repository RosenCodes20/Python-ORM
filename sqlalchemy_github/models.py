from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Relationship

DATABASE = "postgresql+psycopg2://postgres-user:postgres-password@localhost/sqlalchemy"

engine = create_engine(DATABASE)

Base = declarative_base()


class Employee(Base):

    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True
    )

    first_name = Column(
        String(40)
    )

    last_name = Column(
        String(40)
    )

    age = Column(
        Integer
    )

    city_id = Column(
        Integer,
        ForeignKey("cities.id"),
        default=1,
    )

    city = Relationship("City", back_populates="employees")


class City(Base):

    __tablename__ = "cities"

    id = Column(
        Integer,
        primary_key=True
    )

    city = Column(
        String(20)
    )

    employees = Relationship("Employee")


Base.metadata.create_all(engine)