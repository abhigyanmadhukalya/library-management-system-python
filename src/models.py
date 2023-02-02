from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Books(Base):
    __tablename__ = "books"
    id =  Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    issued_by = Column(String, ForeignKey("students.student_id"))

    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

    def __repr__(self):
        return f"({self.id}) {self.title} by {self.author}"

class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    book_issued = Column(Integer)

    def __init__(self, student_id, name, book_issued):
        self.student_id = student_id
        self.name = name
        self.book_issued = book_issued

    def __repr__(self):
        return f"({self.student_id}) {self.name} has borrowed {self.book_issued}"

engine = create_engine("sqlite:///library.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()