from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class University(Base):
    __tablename__ = 'university'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 
class Course(Base):
    __tablename__ = 'course'


    name =Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    professor = Column(String(250))
    school = Column(String(250))
    university_id = Column(Integer,ForeignKey('university.id'))
    university = relationship(University)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'professor'         : self.professor,
           'school'         : self.school,
       }



engine = create_engine('sqlite:///curriculum.db')
 

Base.metadata.create_all(engine)
