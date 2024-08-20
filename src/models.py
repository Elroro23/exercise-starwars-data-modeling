import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(15), unique=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    

class Characters(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    specie = Column(String(20), nullable=False)
    gender = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)

class Planets(Base):
    __tablename__='planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    population = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climated = Column(String(20), nullable=False)
    terrain = Column(String(20), nullable=False)

class Starships(Base):
    __tablename__='starships'
    starship_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=False)
    manufacturer = Column(String(20), nullable=False)
    passengers = Column(Integer, nullable=False)
    pilots = Column(Integer, nullable=False)

class FavoriteCharacter(Base):
    __tablename__='favorite_character'
    favorite_character_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user_id_relationship = relationship(User)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    character_id_relationship = relationship(Characters)

class FavoritePlanet(Base):
    __tablename__='favorite_planet'
    favorite_planet_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user_id_relationship = relationship(User)
    planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    planet_id_relationship = relationship(Planets)

class FavoriteStarship(Base):
    __tablename__='favorite_starship'
    favorite_starship_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user_id_relationship = relationship(User)
    starship_id = Column(Integer, ForeignKey('starships.starship_id'))
    starship_id_relationship = relationship(Starships)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
