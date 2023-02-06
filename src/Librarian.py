from rich import print
import typer
from models import *
from getpass import getpass

class Librarian():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def add_new_books(self):
        self.new_book_name = typer.prompt(text="Enter the name of the book you'd like to add")
        self.new_book_author = typer.prompt(text="Enter the name of the author of the book you'd like to add")
        print(f"Added {self.new_book_name} by {self.new_book_author} to the library")

    def sign_in(self):
        self.username = typer.prompt(text="Enter your username")
        self.password = getpass(prompt="Enter your password: ", stream=None)

    def sign_up(self):
        self.name = typer.prompt(text="Enter your name")
        self.username = typer.prompt(text="Enter your username")
        self.password = getpass(prompt="Enter your password: ", stream=None)
        self.confirm_password = getpass(prompt="Confirm your password: ", stream=None)