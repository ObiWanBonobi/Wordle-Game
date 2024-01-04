"""Google sheets import and library imports"""
import gspread

from google.oauth2.service_account import Credentials
from rich import print as rprint
from rich.panel import Panel
from words import english_words
from countries import country_list
from extras import WORDLE_RULES, TITLE_BANNER

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
            TITLE_BANNER,
            title=":books: A Python Terminal Game :books:",
            subtitle=":books: By Bo de Groot :books:",
            style="bold",
        )
    )
    print()
    rprint(
        Panel(
            WORDLE_RULES,
            title=":clipboard: Rules :clipboard:",
            style="bold",
            subtitle=":cross_mark: :o: :heavy_check_mark:",
        )
    )

    get_user_input()


def get_user_input():
    """
    Input for the users name and country. They will come up with an error if anything
    other than alphabetical letters and spaces are used. The country input will come 
    back with an error if the input doesn't match any of the countries in the countries 
    file.
    """
    while True:
        name_input = input("Enter your name : \n")
        print("Checking if name input is valid...\n")

        if check_input(name_input):
            break

    while True:
        country_input = input("Enter your country : \n")
        print("Checking if country input is valid...\n")

        if check_input(country_input):
            print(f"Hello {name_input.title()} from {country_input.title()}!\n")
            break

    ready_to_play_game()

    return name_input


def ready_to_play_game():
    """
    Asks the user if they're ready to play Wordle. Then exits the game if not. And
    starts the game when they are.
    """
    play_game_input = input("Ready to play? y/n\n")

    if play_game_input.lower() == "y":
        print("Let's play Wordle!\n")
        play_wordle()
    elif play_game_input.lower() == "n":
        print("Exiting game...\n")
        exit()
    else:
        print("Invalid option, type y or n.\n")


def play_wordle():
    """
    Starts playing wordle
    """
    print("playing wordle")


def check_input(values):
    """
    Inside the try, Raises ValueError if the name and country input is something 
    other than an alphabetical letters or spaces.
    """
    try:
        if not all(x.isalpha() or x.isspace() for x in values):
            raise ValueError("The input can only be alphabetical letters and spaces.\n")
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
