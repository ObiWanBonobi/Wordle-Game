"""Google sheets import and library imports"""
import random
import sys
import gspread

from google.oauth2.service_account import Credentials
from rich import print as rprint
from rich.panel import Panel
from words import ENGLISH_LIST
from countries import COUNTRY_LIST
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
    Input for the users name and country. The name input will come up with an error if anything
    other than alphabetical letters and spaces are used. The country input will come back with an
    error if the input doesn't match any of the countries in the countries file.
    """
    while True:
        name_input = input("Enter your name : \n").title()
        print("\nChecking if name input is valid...\n")

        if check_input(name_input):
            break

    while True:
        country_input = input("Enter your country in English : \n").title()
        print("\nChecking if country input is valid...\n")

        if check_country(country_input):
            print(f"Hello {name_input} from {country_input}!\n")
            break

    ready_to_play_game()

    return name_input, country_input


def ready_to_play_game():
    """
    Asks the user if they're ready to play Wordle. Then exits the game if n is pressed, and
    starts the game when y is pressed.
    """
    play_game_input = input("Ready to play? y/n\n").lower()

    if play_game_input == "y":
        print("\nLet's play Wordle!\n")
        play_wordle()
    elif play_game_input == "n":
        print("Exiting game...\n")
        sys.exit()
    else:
        print("Invalid option, type either y or n.\n")


def play_wordle():
    """
    The computer chooses a random word from the imported words list.
    """
    computer_choice = random.choice(ENGLISH_LIST).upper()

    print("You have 6 guesses :\n")

    for guess_num in range(1, 7):
        user_guess = input(f"Guess {guess_num} : ").upper()
        if user_guess == computer_choice:
            print("Correct\n")
            break

        correct_letters = {
        letter for letter, correct in zip(user_guess, computer_choice) if letter == correct
        }
        misplaced_letters = set(user_guess) & set(computer_choice) - correct_letters
        wrong_letters = set(user_guess) - set(computer_choice)

        print("\nCorrect letters:", ", ".join(sorted(correct_letters)))
        print("\nMisplaced letters:", ", ".join(sorted(misplaced_letters)))
        print("\nWrong letters:", ", ".join(sorted(wrong_letters)))


def check_input(name):
    """
    Validation function for name input. Inside the try, Raises ValueError if the name
    input is something other than an alphabetical letters or spaces.
    """
    try:
        if not all(x.isalpha() or x.isspace() for x in name):
            raise ValueError(
                "Name input can only be alphabetical letters and spaces.\n"
            )
    except ValueError as e:
        print(f"Invalid name : {e}Please try again.\n")
        return False

    return True


def check_country(country):
    """
    Validation function for country input. Inside the try, Raises ValueError if the country
    input is not in the countries list.
    """
    try:
        if country not in COUNTRY_LIST:
            raise ValueError(
                "Country input wont work with symbols and or special characters\n"
            )
    except ValueError as e:
        print(f"Invalid country : {e}Please try again.\n")
        return False

    return True


def main():
    """
    Runs all the program functions
    """
    display_start_menu()


get_user_input()
