from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    updated = Column(TIMESTAMP)

    def __repr__(self):
        return 'id: {}, name: {}, age: {}'.format(self.id, self.name, self.age)
