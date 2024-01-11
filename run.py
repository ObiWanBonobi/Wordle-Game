"""Google sheets import and library imports"""

# Random is used for the computer to randomly choose a word from the words list
import random
# Sys is used to close the game correctly
import sys
# Gspread is a Python API for Google Sheets
import gspread
# This module implements the JWT Profile for OAuth 2.0 Authorization Grants
from google.oauth2.service_account import Credentials
# Rich is used for the colourful text
from rich import print as rprint
# Rich panel is used to place the leaderboard in a frame
from rich.panel import Panel
# Rich console is used to set the width of the console
from rich.console import Console
# This connects the validation.py file with this run.py file
import utils.validation as vd


# Sets the with of the display for the console.rule
console = Console(width=79)


# Tells the program what files can be accessed
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


def display_wordle():
    """
    Displays the start page with a fun titel.
    """
    print()
    console.rule("[red]:books:  A Python Terminal Game :books:")
    print(r"""
.------------..------------..------------..-----------..----------..----------.
| ___    ___ ||    ____    || _______    || _______   || _____    || ________ |
||   |  |   |||  .'    `.  |||_   __ \   |||   ___ `. |||_   _|   |||   ___  ||
| | | /\ | | || /  .--.  \ ||  | |__) |  || | |   `. \||  | |     || | |_  \_||
| | |/  \| | || | |    | | ||  |  __ /   || | |    | |||  | |   _ || |  _|  _ |
| |   /\   | || \  `--'  / || _| |  \ \_ || | |___.' /|| _| |__/ ||| | |___/ ||
| |__/  \__| ||  `.____.'  |||____| |___||||_______.' |||________||||________||
|            ||            ||            ||           ||          ||          |
'------------''------------''------------''-----------''----------''----------'
    """)
    console.rule("[red]:books:  By Bo de Groot :books:")
    print()


def show_rules():
    """
    Shows the rules when asked for. When 'y' is pressed it wil show the rules,
    then it will get the user name. When 'n' is pressed, the rules will be
    skipped.
    """
    read_rules = ""
    while read_rules not in ("y", "n"):
        read_rules = input("Do you want to read the rules? y/n\n").lower()

        if read_rules == "y":
            print()
            console.rule("[red]:clipboard:  Rules :clipboard:")
            print("""
To start the game :
- First add your name. Make sure your name is only created with alphabetical
  letters.
- Then fill in the country you're from, make sure it's a real country.
- To play the game, you have to enter a real 5 letter English word. If the
  wrong letter got quessed, it will show a red cross. When you guess a correct
  letter but its in the wrong spot, it will show a red circle. If the letter is
  correct and in the correct spot, it will show a green check mark. Guess the
  correct 5 letter word.
            """)
            console.rule("[red]:cross_mark: :o: :heavy_check_mark: ")
            print()
        elif read_rules == "n":
            print()
        else:
            print("Invalid option, type either y or n.\n")


def get_user_input():
    """
    Input for the users name and country. Starts the game after a 'hello'
    message.
    """
    console.rule("[red]User Data :")
    print()

    while True:
        # Changes user input to a Capital name
        name_input = input("Enter your name : \n").title()
        print("\nChecking if name is valid...\n")

        if vd.check_name_input(name_input):
            break

    while True:
        # Changes user input to a Capital country
        country_input = str(input(
            "Enter your country in English : \n")).title()
        print("\nChecking if country is valid...\n")

        if vd.check_country_input(country_input):
            print(f"Hello {name_input} from {country_input}!")
            break

    print()
    play_wordle(name_input, country_input)


def play_wordle(name, country):
    """
    Starts the wordle game. The computer chooses a random word from the
    imported words list. The user can start guessing 5 letter words. The score
    goes up one point if it's a real word. And prints the word with
    corresponding emojis underneath the input word. When the user guesses the
    word correctly or after 6 tries the user will see a "congrats" or "you
    lose" message.
    """
    computer_choice = random.choice(vd.read_file("words", "txt"))
    score = 0

    console.rule("[red]You have 6 guesses to find the 5 letter word :")
    print()

    for guesses_left in range(1, 7):
        while True:
            user_guess = input(f"Guess {guesses_left} : \n").upper()
            ug = user_guess
            # I did not use a feedback here for a cleaner look
            print()

            if vd.check_user_input(user_guess):
                # Adds one point after every guess
                score += 1
                break

        # Reprints the user word with spaces and corresponding emojis under
        print(f"  {ug[0]}  {ug[1]}  {ug[2]}  {ug[3]}  {ug[4]}")
        rprint(f"{check_letters_word(user_guess, computer_choice)}\n")

        if user_guess == computer_choice:
            rprint("[on green]    Congrats, you guessed the correct word!    ")
            update_leaderboard(name, country, score)
            break

    else:
        # Adds one final point and prints you lost message
        score += 1
        rprint(
            f"[on red]    You lost. The correct word was {computer_choice}    "
        )
        update_leaderboard(name, country, score)


def play_game_again():
    """
    Asks the user if they want to play Wordle again. Then exits the game if 'n'
    is pressed, and starts the game again when 'y' is pressed.
    """
    play_game_input = ""
    while play_game_input not in ("y", "n"):
        play_game_input = input("Do you want to play again? y/n\n").lower()

        if play_game_input == "y":
            print("\nLet's play Wordle!\n")
            get_user_input()
        elif play_game_input == "n":
            print("Exiting game...\n")
            sys.exit()
        else:
            print("Invalid option, type either y or n.\n")


def check_letters_word(user, computer):
    """
    Checks if the letters are :
    - correct and in the correct spot and places a check mark emoji
    - if they are in the word and places a circle emoji
    - if they are not in the word and places a cross mark emoji
    """
    emoji = ""

    for index, letter in enumerate(user):
        # Places a green check emoji under correct letter
        if letter == computer[index]:
            emoji += " :heavy_check_mark: "
        # Places a red circle under letter in incorrect spot
        elif letter in computer:
            emoji += " :o: "
        # Places a red  cross under incorrect letters
        else:
            emoji += " :cross_mark: "

    return emoji


def update_leaderboard(name, country, score):
    """
    Updates the leaderboard Google sheet with the name, country and score.
    Adds one row every time.
    """
    leaderboard_sheet = SHEET.worksheet("leaderboard")
    leaderboard_sheet.append_row(values=[name, country, score])

    show_leaderboard()


def show_leaderboard():
    """
    Asks the user if they want to see the leaderboard. When 'n' is pressed
    the user gets the "play again" question.
    """
    print()
    leaderboard = ""
    while leaderboard not in ("y", "n"):
        leaderboard = input(
            "Do you want to see the leaderboard? y/n\n").lower()
        print()

        if leaderboard == "y":
            print("\nLet's see if you made it on the leaderboard...\n")
            get_leaderboard()
        elif leaderboard == "n":
            play_game_again()
        else:
            print("Invalid option, type either y or n.\n")


def get_leaderboard():
    """
    Shows the top 10 users with the lowest guesses from the leaderboard sheet.
    This function was partly copied from Pedro Cristo. Look in readme.
    """
    # Gets all the values under the "header" in the google sheet
    leaderboard = SHEET.worksheet("leaderboard").get_all_values()[1:]

    for data in leaderboard:
        data[1] = data[1]

    # Gets the top 10 lowest numbers from google sheet
    top_score = sorted(leaderboard, key=lambda x: int(x[2]), reverse=False)

    if len(top_score) < 10:
        count = len(top_score)
    else:
        count = 10

    console.rule("[red]Top 10 lowest guesses :")
    print()

    # Prints the top 10 lowest scores from the google sheet
    for i in range(0, count):
        rprint(Panel(f"""{i+1}\t{top_score[i][0]} \tfrom\t{top_score[i][1]}
        Guesses :\t{top_score[i][2]}"""))

    print()
    play_game_again()


def main():
    """
    Starts the wordle game functions.
    """
    display_wordle()
    show_rules()
    get_user_input()


main()
