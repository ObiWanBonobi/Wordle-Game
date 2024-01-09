"""Google sheets import and library imports"""
import random
import sys
import gspread

from google.oauth2.service_account import Credentials
from rich import print as rprint
from rich.panel import Panel


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
    title_banner = r"""
    .--------------..--------------..--------------..--------------..--------------..--------------.
    | _____  _____ ||     ____     ||  _______     ||  ________    ||   _____      ||  _________   |
    ||_   _||_   _|||   .'    `.   || |_   __ \    || |_   ___ `.  ||  |_   _|     || |_   ___  |  |
    |  | | /\ | |  ||  /  .--.  \  ||   | |__) |   ||   | |   `. \ ||    | |       ||   | |_  \_|  |
    |  | |/  \| |  ||  | |    | |  ||   |  __ /    ||   | |    | | ||    | |   _   ||   |  _|  _   |
    |  |   /\   |  ||  \  `--'  /  ||  _| |  \ \_  ||  _| |___.' / ||   _| |__/ |  ||  _| |___/ |  |
    |  |__/  \__|  ||   `.____.'   || |____| |___| || |________.'  ||  |________|  || |_________|  |
    |              ||              ||              ||              ||              ||              |
    '--------------''--------------''--------------''--------------''--------------''--------------'
    """

    wordle_rules = """
    To start the game :
    - First add your name. Make sure your name is only created with alphabetical letters.
    - Then fill in the County you're from, make sure it's a real country.
    - To play the game, you have to enter a real 5 letter English word. If the wrong letter got quessed, 
    it will show a red cross. When you guess a correct letter but its in the wrong spot, it will show a 
    red circle. If the letter is correct and in the correct spot, it will show a green check mark. 
    """

    rprint(Panel(title_banner, style="bold",
            title=":books: A Python Terminal Game :books:",
            subtitle=":books: By Bo de Groot :books:"))
    print()
    rprint(Panel(wordle_rules, style="bold",
            title=":clipboard: Rules :clipboard:",
            subtitle=":cross_mark: :o: :white_check_mark:"))


def get_user_input():
    """
    Input for the users name and country. The name input will come up with an error if anything
    other than alphabetical letters and spaces are used. The country input will come back with an
    error if the input doesn't match any of the countries in the countries file, also can't have
    any special characters and or symbols.
    """
    while True:
        name_input = input("Enter your name : \n").title()
        print("\nChecking if name is valid...\n")

        if check_name_input(name_input):
            break

    while True:
        country_input = input("Enter your country in English : \n").title()
        print("\nChecking if country is valid...\n")

        if check_country_input(country_input):
            print(f"Hello {name_input} from {country_input}!\n")
            update_leaderboard(name_input, 1)
            update_leaderboard(country_input, 2)
            break

    play_wordle()
    return name_input, country_input


def play_game_again():
    """
    Asks the user if they want to play Wordle again. Then exits the game if n is pressed, and
    starts the game again when y is pressed.
    """
    play_game_input = input("Ready to play? y/n\n").lower()

    if play_game_input == "y":
        print("\nLet's play Wordle!\n")
        get_user_input()
    elif play_game_input == "n":
        print("Exiting game...\n")
        sys.exit()
    else:
        print("Invalid option, type either y or n.\n")


def play_wordle():
    """
    Starts the wordle game. The computer chooses a random word from the imported words list.
    The user can start guessing 5 letter words, that get checked if they're real 5 letter
    words. The score goes up one point. And prints the word with emojis to the terminal.
    """
    with open("text_files/words.txt", "r", encoding="cp1252") as f:
        all_words = f.read()
        words = list(map(str, all_words.upper().split()))

    computer_choice = random.choice(words)
    score = 0

    print("You have 6 guesses to find the 5 letter word :\n")

    for guesses_left in range(1, 7):
        while True:
            user_guess = input(f"Guess {guesses_left} : ").upper()
            ug = user_guess
            score += 1
            print()

            if check_user_input(user_guess):
                break

        print(f" {ug[0]}  {ug[1]}  {ug[2]}  {ug[3]}  {ug[4]}")
        rprint(f"{check_letters_word(user_guess, computer_choice)}\n")

        if user_guess == computer_choice:
            print("Congratulations, you guessed the correct word!\n")
            update_leaderboard(score, 3)
            get_leaderboard()
            print()
            print("Do you want to play again?\n")
            play_game_again()
            break

    else:
        score = 7
        print(f"The correct word was {computer_choice}\n")
        update_leaderboard(score, 3)
        get_leaderboard()
        print()
        print("Do you want to play again?\n")
        play_game_again()


def check_letters_word(user, computer):
    """
    Checks if the letters are :
    - correct and in the correct spot and places a corresponding emoji
    - if they are in the word and places a corresponding emoji
    - if they are not in the word and places a corresponding emoji
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
    country_input_strip = country.strip()

    with open("text_files/countries.csv", "r", encoding="cp1252") as f:
        country_file = f.read()

        try:
            if country_input_strip not in country_file:
                raise ValueError(
                    "Country input wont work with symbols and or special characters,")
        except ValueError as e:
            print(f"Invalid country : {e} please try again.\n")
            return False

    return True


def check_user_input(user):
    """
    Validation function for user input. Inside the try, Raises ValueError if the input
    is not in the words list.
    """
    with open("text_files/all_words.txt", "r", encoding="cp1252") as f:
        all_words_list = f.read()
        all_words = list(map(str, all_words_list.upper().split()))

        try:
            if user not in all_words:
                raise ValueError("The word needs to be a real 5 alphabetical letter word,")
        except ValueError as e:
            print(f"Invalid word : {e} please try again.\n")
            return False

    return True


def update_leaderboard(data, cell):
    """
    Updates the leaderboard Goodle sheet with the name, country and score
    """
    leaderboard_sheet = SHEET.worksheet("leaderboard")
    column_values = leaderboard_sheet.col_values(cell)
    column_numbers = len(column_values) + 1
    leaderboard_sheet.update_cell(column_numbers, cell, data)


def get_leaderboard():
    """
    Shows the last 10 users on the leaderboard after the game is finished.
    """
    leaderboard = SHEET.worksheet("leaderboard").get_all_values()[1:]

    for data in leaderboard:
        data[1] = data[1]

    update_data = sorted(leaderboard, key=lambda x: int(x[2]), reverse=False)
    ud = update_data

    if len(update_data) < 10:
        count = len(update_data)
    else:
        count = 10

    rprint(Panel("Top 10 lowest guesses :\n"))

    for i in range(0, count):
        rprint(Panel(f"""{i+1}\t{ud[i][0]} \tfrom\t{ud[i][1]}
        Guesses :\t{ud[i][2]}"""))
    print()


def main():
    """
    Runs all the program functions
    """
    display_start_menu()
    get_user_input()


main()
