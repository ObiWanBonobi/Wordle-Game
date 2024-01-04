"""Google sheets import and library imports"""
import re
import gspread

from google.oauth2.service_account import Credentials
from rich import print as rprint
from rich.panel import Panel
from words import english_words
from countries import country_list
from extras import wordle_rules, title_banner

# API setup
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

# Credentials and access to google sheets
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("wordle_bo")


def display_start_menu():
    """
    Displays the start page with a fun titel and the name input
    """
    rprint(
        Panel(
            title_banner,
            title=":books: A Python Terminal Game :books:",
            subtitle=":books: By Bo de Groot :books:",
            style="bold",
        )
    )
    print()
    rprint(
        Panel(
            wordle_rules,
            title=":clipboard: Rules :clipboard:",
            style="bold",
            subtitle=":cross_mark: :o: :heavy_check_mark:",
        )
    )

    get_input()


def get_input():
    """
    Input for the users name and country. The name input will come up
    with an error if numbers are used and if the name is longer than
    10 letters. The country input will come back with an error if the
    user types in an non-existing country.
    """
    while True:
        name_input = input("Enter your name : \n")
        print("Checking if name input is valid...\n")

        if check_input(name_input):
            print("nice")
            break

    return name_input


def check_input(values):
    """
    Inside the try, Raises ValueError if the name input is something other than
    alphabetical letters.
    """
    try:
        if not re.match(r"^[A-Za-z]+$", values):
            raise ValueError("The name input can only be alphabetical letters.\n")
    except ValueError as e:
        print(f"Invalid data: {e}Please try again.\n")
        return False

    return True


def main():
    """
    Runs all the program functions
    """
    display_start_menu()


main()
