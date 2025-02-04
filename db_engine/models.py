from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))  
    grades = relationship('Grade', back_populates='student') 
    group = relationship('Group', back_populates='students') 

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', back_populates='group')  

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subjects = relationship('Subject', back_populates='teacher')  

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id')) 
    teacher = relationship('Teacher', back_populates='subjects')  
    grades = relationship('Grade', back_populates='subject')  

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))  
    subject_id = Column(Integer, ForeignKey('subjects.id')) 
    score = Column(Integer)
    date_received = Column(Date)

    student = relationship('Student', back_populates='grades')  
    subject = relationship('Subject', back_populates='grades')  