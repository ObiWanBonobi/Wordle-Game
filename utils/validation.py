"""
All the validation for the user inputs is contained in this file.
"""

# Sys is used to close the game correctly
import sys
# Time is used for the delete_error_message function, so after 2 seconds the
# last error message gets deleted
from time import sleep


def read_file(name, types):
    """
    Gets data from csv and txt file. Comes back with error message when file is
    not found.
    """
    if types == "csv":
        # Opens csv file then splits and reads it
        with open(f"text_files/{name}.{types}", "r", encoding="cp1252") as f:
            country_list = f.read().split(",")
            return country_list
    elif types == "txt":
        # Opens a txt file then makes the words uppercase and splits and
        # reads it.
        with open(f"text_files/{name}.{types}", "r", encoding="cp1252") as f:
            words_list = [word.upper() for word in f.read().split()]
            return words_list
    else:
        print("Error, invalid file")


def check_name_input(name):
    """
    Validation function for name input. Inside the try, Raises ValueError if
    the name input is something other than alphabetical letters or spaces.
    """
    try:
        # If input is not a letter or a space it calls an error
        if not all(x.isalpha() or x.isspace() for x in name):
            raise ValueError(
                "Name can only be alphabetical letters and spaces")
        # If the input is less than 2 letters it calls an error
        if len(name) < 2:
            raise ValueError("Name needs more than 2 letters")
    except ValueError as e:
        print(f"Invalid name : \n{e}\nPlease try again.\n")
        return False

    return True


def check_country_input(country):
    """
    Validation function for country input. Inside the try, Raises ValueError if
    the country input is not in the countries list.
    """
    try:
        # If input is not in the countries file it calls an error
        if country not in read_file("countries", "csv"):
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
    the input is not in the words list. I kept this a single line so the error
    message can be deleted after 2 seconds so the user can see their
    previous guesses better.
    """
    try:
        # If input is not in the all_words list it calls an error
        if user not in read_file("all_words", "txt"):
            raise ValueError("Input needs to be a real 5 letter word,")
    except ValueError as e:
        print(f"Invalid word : {e} try again.")
        # Deletes the above message after 2 seconds
        delete_error_message()
        return False

    return True


def delete_error_message():
    """
    Deletes the last error message in the terminal for better visuals.
    This function was partly copied from website. Look in readme.
    """
    # Counts 2 seconds then deletes previous printed message
    sleep(2)
    sys.stdout.write("\x1b[1A")
    sys.stdout.write("\x1b[2K")
