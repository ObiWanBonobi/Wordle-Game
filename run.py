"""Google sheets import and library imports"""
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
    Displays the start page with a fun titel
    """
    title_banner = """
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

    rprint(
        Panel(
            title_banner,
            title=":books: A Python Terminal Game :books:",
            subtitle=":books: By Bo de Groot :books:",
        )
    )


display_start_menu()
