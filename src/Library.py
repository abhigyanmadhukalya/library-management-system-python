from rich import print
from models import *
from sqlalchemy.orm import sessionmaker

class Library:
    def __init__(self, availablebooks):
            self.availablebooks = session.query(Books).all()

    def display_available_books(self):
                   print("The books we have in our library are as follows:")
                   for book in self.availablebooks:
                         print(book)
    def lend_book(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been borrowed")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library")

    def add_book(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thanks for returning your borrowed book")