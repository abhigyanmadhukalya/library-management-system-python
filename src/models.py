from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Books(Base):
    __tablename__ = "books"
    id =  Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

    def __repr__(self):
        return f"({self.id}) {self.title} by {self.author}"

engine = create_engine("sqlite:///library.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()