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
            subtitle=":cross_mark: :o: :white_check_mark:",
        )
    )


def get_user_input():
    """
    Input for the users name and country. The name input will come up with an error if anything
    other than alphabetical letters and spaces are used. The country input will come back with an
    error if the input doesn't match any of the countries in the countries file.
    """
    while True:
        name_input = input("Enter your name : \n").title()
        print("\nChecking if name input is valid...\n")

        if check_name_input(name_input):
            break

    while True:
        country_input = input("Enter your country in English : \n").title()
        print("\nChecking if country input is valid...\n")

        if check_country_input(country_input):
            print(f"Hello {name_input} from {country_input}!\n")
            update_leaderboard(name_input, country_input)
            break

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
    Starts the wordle game. The computer chooses a random word from the imported words list.
    The user can start guessing 5 letter words.
    """
    computer_choice = random.choice(ENGLISH_LIST).upper()
    score = 0

    print("You have 6 guesses to find the 5 letter word :\n")
    print(computer_choice)

    for guesses_left in range(1, 7):
        while True:
            user_guess = input(f"Guess {guesses_left} : \n").upper()
            ug = user_guess
            score += 1
            print()

            if check_user_input(user_guess):
                break

        print(f" {ug[0]}  {ug[1]}  {ug[2]}  {ug[3]}  {ug[4]}")
        rprint(f"{check_letters_word(user_guess, computer_choice)}\n")

        if user_guess == computer_choice:
            print("Congratulations, you guessed the correct word!\n")
            print("Do you want to play again?")
            update_leaderboard_score(int(score))
            ready_to_play_game()
            break

    else:
        print(f"The correct word was {computer_choice}\n")


def check_letters_word(user, computer):
    """
    Checks if the letters are correct and in the correct spot. If they are in the
    word and if they are not in the word.
    """
    emoji = ""

    for index, letter in enumerate(user):
        if letter == computer[index]:
            emoji += ":white_check_mark: "
        elif letter in computer:
            emoji += ":o: "
        else:
            emoji += ":cross_mark: "

    return emoji


def check_name_input(name):
    """
    Validation function for name input. Inside the try, Raises ValueError if the name
    input is something other than an alphabetical letters or spaces.
    """
    try:
        if not all(x.isalpha() or x.isspace() for x in name):
            raise ValueError("Name input can only be alphabetical letters and spaces,")
    except ValueError as e:
        print(f"Invalid name : {e} please try again.\n")
        return False

    return True


def check_country_input(country):
    """
    Validation function for country input. Inside the try, Raises ValueError if the country
    input is not in the countries list.
    """
    try:
        if country not in COUNTRY_LIST:
            raise ValueError(
                "Country input wont work with symbols and or special characters,"
            )
    except ValueError as e:
        print(f"Invalid country : {e} please try again.\n")
        return False

    return True


def check_user_input(user):
    """
    Validation function for user input. Inside the try, Raises ValueError if the input
    is more or less than 5 letters and not in the words list.
    """
    try:
        if len(user) != 5:
            raise ValueError("The word needs to be 5 alphabetical letters long,")
        if user not in ENGLISH_LIST:
            raise ValueError("The word needs to be a real 5 letter word,")
    except ValueError as e:
        print(f"Invalid word : {e} please try again.\n")
        return False

    return True


def update_leaderboard(name, country):
    """
    Updates the leaderboard sheet with the users name and country
    """
    update_leaderboard_sheet = SHEET.worksheet("leaderboard")
    update_leaderboard_sheet.append_row([name, country])


def update_leaderboard_score(score):
    """
    Updates the leaderboard sheet with the user score
    """
    leaderboard_sheet = SHEET.worksheet("leaderboard")
    column_values = leaderboard_sheet.col_values(3)
    column_numbers = len(column_values) + 1
    leaderboard_sheet.update_cell(column_numbers, 3, score)


def main():
    """
    Runs all the program functions
    """
    display_start_menu()
    get_user_input()
    ready_to_play_game()


main()
