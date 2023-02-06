import typer
from Library import *
from Pupil import *
from Librarian import *
from rich import print, traceback
from inquirer import prompt, List
from models import *
from sqlalchemy.orm import sessionmaker

traceback.install()

def administrative_options():
    options = [
        List(
            "admin_options",
            message="What would you like to do?",
            choices=[
                "Sign in",
                "Sign up",
                "Add new books",
            ]
        )
    ]
    admin_answers = prompt(options)
    if admin_answers["admin_options"] == "Sign in":
        librarian.sign_in()
    elif admin_answers["admin_options"] == "Sign up":
        librarian.sign_up()
    elif admin_answers["admin_options"] == "Add new books":
        librarian.add_new_books()

def main():

    library = Library()
    pupil = Pupil()
    librarian = Librarian()

    questions = [
        List(
            "actions",
            message="What would you like to do?",
            choices=[
                        "List books",
                        "Borrow a book",
                        "Return a book",
                        "Administrative Options"
                    ],
        )
    ]

    answers = prompt(questions)
    if answers["actions"] == "List books":
        print(books)
    elif answers["actions"] == "Borrow a book":
        pupil.request_book()
    elif answers["actions"] == "Return a book":
        pupil.return_book()
    elif answers["actions"] == "Administrative Options":
        administrative_options()


if __name__ == "__main__":
    typer.run(main)

