from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, Relationship

DATABASE = ""

engine = create_engine(DATABASE)

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
    )

    ingredients = Column(
        Text,
    )

    instructions = Column(
        Text,
    )

    chef_id = Column(
        Integer,
        ForeignKey(
            "chefs.id",
            ondelete="CASCADE"
        )
    )

    chef = Relationship(
        "Chef",
        back_populates="recipes"
    )


class Chef(Base):
    __tablename__ = "chefs"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String
    )

    recipes = Relationship(
        Recipe,
        back_populates="chef"
    )


Base.metadata.create_all(engine)
