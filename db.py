import datetime
import os
import time

from typing import List

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import TIMESTAMP, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class ModelBase(DeclarativeBase):

    last_modified: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())

    def as_dict (self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def is_outdated(self, timestamp):
        # convert last_modified to a unix timestamp for easy comparison
        lm_time = time.mktime(self.last_modified.timetuple())
        return lm_time >= timestamp

db = SQLAlchemy(app, model_class=ModelBase)

def create_db():
    with app.app_context():
        db.create_all()

class Character(db.Model):
    __tablename__ = "character"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    name: Mapped[str] = mapped_column()
    
    stats: Mapped[List["CharacterStat"]] = relationship(back_populates="character", lazy="selectin")
    skills: Mapped[List["CharacterSkill"]] = relationship(back_populates="character", lazy="selectin")
    health: Mapped[List["Health"]] = relationship(back_populates="character", lazy="selectin")
    armor: Mapped[List["Armor"]] = relationship(back_populates="character", lazy="selectin")

    def as_dict(self):
        result = super().as_dict()

        result['stats'] = [r.as_dict() for r in self.stats]
        result['skills'] = [r.as_dict() for r in self.skills]
        result['health'] = [r.as_dict() for r in self.health]
        result['armor'] = [r.as_dict() for r in self.armor]

        return result

class Stat(db.Model):
    __tablename__ = "stat"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column()

class CharacterStat(db.Model):
    __tablename__ = "character_stat"

    id: Mapped[int] = mapped_column(primary_key=True)

    stat_id = mapped_column(ForeignKey("stat.id"))
    stat: Mapped[Stat] = relationship(lazy="selectin")
    
    character_id = mapped_column(ForeignKey("character.id"))
    character: Mapped[Character] = relationship(back_populates="stats")
    
    value: Mapped[int] = mapped_column()

    # last_modified: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())

    def as_dict(self):
        result = super().as_dict()

        result['name'] = self.stat.name

        return result

class Skill(db.Model):
    __tablename__ = "skill"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    stat_id = mapped_column(ForeignKey("stat.id"))
    stat: Mapped[Stat] = relationship(lazy="selectin")
    
    name: Mapped[str] = mapped_column()

    def as_dict(self):
        result = super().as_dict()

        result['stat'] = self.stat.name

        return result

class CharacterSkill(db.Model):
    __tablename__ = "character_skill"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    skill_id = mapped_column(ForeignKey("skill.id"))
    skill: Mapped[Skill] = relationship(lazy="selectin")
    
    character_id = mapped_column(ForeignKey("character.id"))
    character: Mapped[Character] = relationship(back_populates="skills")
    
    value = db.Column(db.Integer)

    def as_dict(self):
        result = super().as_dict()

        result['name'] = self.skill.name
        result['stat'] = self.skill.stat.name

        return result

class Health(db.Model):
    __tablename__ = "health"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    character_id = mapped_column(ForeignKey("character.id"))
    character: Mapped[Character] = relationship(back_populates="health")

    location: Mapped[str] = mapped_column()
    hp: Mapped[int] = mapped_column()

    def update_hp(self, hp, timestamp):
        if not self.is_outdated(timestamp):
            self.hp = hp

class Armor(db.Model):
    __tablename__ = "armor"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    character_id = mapped_column(ForeignKey("character.id"))
    character: Mapped[Character] = relationship(back_populates="armor")

    location: Mapped[str] = mapped_column()
    hp: Mapped[int] = mapped_column()

    def update_hp(self, hp, timestamp):
        if not self.is_outdated(timestamp):
            self.hp = hp

