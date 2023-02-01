from Library import *
from Pupil import *
import typer
from rich import print, traceback
from inquirer import prompt, List

traceback.install()

def main():

    library = Library()
    pupil = Pupil()

    questions = [
        List(
            "actions",
            message="What would you like to do?",
            choices=["List books", "Borrow a book", "Return a book"],
        )
    ]

    answers = prompt(questions)



if __name__ == "__main__":
    typer.run(main)