"""Google sheets import and library imports"""
import random
import sys
import gspread

from google.oauth2.service_account import Credentials
from rich import print as rprint
from rich.panel import Panel
from rich.console import Console
console = Console(width=78)


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


def display_wordle():
    """
    Displays the start page with a fun titel and starts the rules function.
    """
    print()
    console.rule("[red]:books: A Python Terminal Game :books:")
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
    console.rule("[red]:books: By Bo de Groot :books:")
    print()

    show_rules()


def show_rules():
    """
    Shows the rules when asked for. When y is pressed it wil show the rules,
    then it will get the user name. When n is pressed, the rules will be
    skipped.
    """
    read_rules = input("Do you want to read the rules? y/n\n").lower()

    if read_rules == "y":
        print()
        console.rule("[red]:clipboard: Rules :clipboard:")
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
        console.rule("[red]:cross_mark: :o: :white_check_mark: ")
        print()
        get_user_input()
    elif read_rules == "n":
        print()
        get_user_input()
    else:
        print("Invalid option, type either y or n.\n")


def get_user_input():
    """
    Input for the users name and country. The name input will come up with an
    error if anything other than alphabetical letters and spaces are used. The
    country input will come back with an error if the input doesn't match any
    of the countries in the countries file, also can't have any special
    characters and or symbols. Then updates the Google leaderboard sheet with
    the name and country.
    """
    console.rule("[red]User Data :")
    print()

    while True:
        name_input = input("Enter your name : \n").title()
        print("\nChecking if name is valid...\n")

        if check_name_input(name_input):
            break

    while True:
        country_input = input("Enter your country in English : \n").title()
        print("\nChecking if country is valid...\n")

        if check_country_input(country_input):
            print(f"Hello {name_input} from {country_input}!")
            update_leaderboard(name_input, 1)
            update_leaderboard(country_input, 2)
            break

    print()
    play_wordle()
    return name_input, country_input


def play_wordle():
    """
    Starts the wordle game. The computer chooses a random word from the
    imported words list. The user can start guessing 5 letter words, that get
    checked if the input is a real 5 letter word. The score goes up one point
    if it's a real word. And prints the word with corresponding emojis
    underneath the input word. When the user guesses the word correctly or
    after 6 tries the user will be asked if they want to see the leaderboard.
    """
    with open("text_files/words.txt", "r", encoding="cp1252") as f:
        all_words = f.read()
        words = list(map(str, all_words.upper().split()))

    computer_choice = random.choice(words)
    score = 0

    console.rule("[red]You have 6 guesses to find the 5 letter word :")
    print()

    for guesses_left in range(1, 7):
        while True:
            user_guess = input(f"Guess {guesses_left} : \n").upper()
            ug = user_guess
            print()

            if check_user_input(user_guess):
                score += 1
                break

        print(f"  {ug[0]}  {ug[1]}  {ug[2]}  {ug[3]}  {ug[4]}")
        rprint(f"{check_letters_word(user_guess, computer_choice)}\n")

        if user_guess == computer_choice:
            rprint(
                "[on green]    Congrats, you guessed the correct word!    "
                )
            update_and_show_leaderboard(score)
            break

    else:
        score += 1
        rprint(
            f"[on red]    You lost. The correct word was {computer_choice}    "
        )
        update_and_show_leaderboard(score)


def play_game_again():
    """
    Asks the user if they want to play Wordle again. Then exits the game if n
    is pressed, and starts the game again when y is pressed.
    """
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
        if letter == computer[index]:
            emoji += " :white_check_mark: "
        elif letter in computer:
            emoji += " :o: "
        else:
            emoji += " :cross_mark: "

    return emoji


def check_name_input(name):
    """
    Validation function for name input. Inside the try, Raises ValueError if
    the name input is something other than alphabetical letters or spaces.
    """
    try:
        if not all(x.isalpha() or x.isspace() for x in name):
            raise ValueError(
                "Name can only be alphabetical letters and spaces")
    except ValueError as e:
        print(f"Invalid name : \n{e}\nPlease try again.\n")
        return False

    return True


def check_country_input(country):
    """
    Validation function for country input. Inside the try, Raises ValueError if
    the country input is not in the countries list.
    """
    country_input_strip = country.strip()

    with open("text_files/countries.csv", "r", encoding="cp1252") as f:
        country_file = f.read()

        try:
            if country_input_strip not in country_file:
                raise ValueError(
                    "Country name wont work with symbols or special characters"
                    )
        except ValueError as e:
            print(f"Invalid country : \n{e}\nPlease try again.\n")
            return False

    return True


def check_user_input(user):
    """
    Validation function for user input. Inside the try, Raises ValueError if
    the input is not in the words list.
    """
    with open("text_files/all_words.txt", "r", encoding="cp1252") as f:
        all_words_list = f.read()
        all_words = list(map(str, all_words_list.upper().split()))

        try:
            if user not in all_words:
                raise ValueError(
                    "Input needs to be a real 5 alphabetical letter word")
        except ValueError as e:
            print(f"Invalid word : \n{e}\nPlease try again.\n")
            return False

    return True


def update_leaderboard(data, cell):
    """
    Updates the leaderboard Google sheet with the name, country and score
    """
    leaderboard_sheet = SHEET.worksheet("leaderboard")
    column_values = leaderboard_sheet.col_values(cell)
    column_numbers = len(column_values) + 1
    leaderboard_sheet.update_cell(column_numbers, cell, data)


def update_and_show_leaderboard(data):
    """
    First updates the score inside the leaderboard sheet. Then asks the user if
    they want to see the leaderboard. It asks the user if they want to play the
    game again if n is pressed, and if y is pressed will show the leaderboard
    asks the user if they want to play the game again.
    """
    update_leaderboard(data, 3)

    print()
    leaderboard = input("Do you want to see the leaderboard? y/n\n").lower()
    print()

    if leaderboard == "y":
        print("\nLet's see if you made the leaderboard...\n")
        get_leaderboard()
    elif leaderboard == "n":
        play_game_again()
    else:
        print("Invalid option, type either y or n.\n")


def get_leaderboard():
    """
    Shows the top 10 users with the lowest guesses from the leaderboard sheet
    after y is pressed by the user in the update_and_show_leaderboard function.
    """
    leaderboard = SHEET.worksheet("leaderboard").get_all_values()[1:]

    for data in leaderboard:
        data[1] = data[1]

    top_score = sorted(leaderboard, key=lambda x: int(x[2]), reverse=False)

    if len(top_score) < 10:
        count = len(top_score)
    else:
        count = 10

    console.rule("[red]Top 10 lowest guesses :")
    print()

    for i in range(0, count):
        rprint(Panel(f"""{i+1}\t{top_score[i][0]} \tfrom\t{top_score[i][1]}
        Guesses :\t{top_score[i][2]}"""))

    print()
    play_game_again()


def main():
    """
    Starts the wordle game with the display first.
    """
    display_wordle()


main()
