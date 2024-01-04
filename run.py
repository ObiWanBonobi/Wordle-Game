"""Google sheets import and library imports"""
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
    Displays the start page with a fun titel
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


def main():
    """
    Runs all the program functions
    """
    display_start_menu()


main()
