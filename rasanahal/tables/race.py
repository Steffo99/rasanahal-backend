from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declared_attr


class Race:
    __tablename__ = 'race'

    @declared_attr
    def rid(self):
        return Column(Integer, primary_key=True)

    @declared_attr
    def name(self):
        return Column(String, nullable=False, unique=True)

    @declared_attr
    def desc(self):
        return Column(String, nullable=False)

    @declared_attr
    def characters(self):
        return relationship("Character", back_populates="race")

    def json(self, minimal):
        return {
            'id': self.rid,
            'name': self.name,
            'desc': self.desc,
            'characters': [char.character.cid if minimal else char.character.json(True) for char in self.characters]
        }
