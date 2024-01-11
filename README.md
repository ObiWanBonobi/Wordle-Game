# Wordle

![Wordle gif](assets/gif/gif_wordle.gif)

[Click on this link to visit the Github page](https://obiwanbonobi.github.io/PP3/)

[Click on this link to play the game on Heroku](https://wordle-bo-abd372c9b403.herokuapp.com/)

<br>


# Content

- [Introduction](#introduction)
    * [User experience](#user-experience)
    * [My vision for the game](#my-vision-for-the-game)
- [Features](#features)
- [Future features](#future-features)
- [Design](#design)
- [Technologies used](#technologies-used)
    * [Lucid Flowchart](#lucid-flowchart)
    * [Google Sheets](#google-sheets)
    * [Libraries](#libraries)
- [Testing](#testing)
    * [Python validation](#python-validation)
    * [HTML validation](#html-validation)
- [Bug fixes](#bug-fixes)
- [Deployment](#deployment)
    * [Github deployment](#github-deployment)
    * [Heroku deployment](#heroku-deployment)
- [Credits](#credits)

<br>


# Introduction

 I'm thrilled to present my very own Python-based Wordle game that promises to challenge and entertain you in equal measure. Dive into the realm of word-guessing, where you'll be tasked with unraveling a hidden five-letter word through strategic deduction and clever guessing. The users final "score" will be shown in the leaderboard option, if the user scores high enough.


## User experience

Wordle is a simple yet engaging word puzzle game that has gained popularity for its straightforward gameplay and addictive nature. That's why I decided to make my own version. The user experience for my Wordle game has been crafted to ensure both enjoyment and ease of play. The game is made for people who want to embark on a captivating journey of word discovery.


## My vision for the game

In envisioning the Wordle game, my goal was to cultivate an engaging and intellectually stimulating experience for players. I designed the game to strike a perfect balance between challenge and enjoyment. The core concept centers around guessing a hidden five-letter word within a limited number of attempts, fostering a sense of accomplishment when the correct word is uncovered. To enhance the game's appeal, I incorporated a diverse and dynamic word bank, keeping players on their toes with an ever-evolving linguistic challenge.

<br>


# Features

<details>
<summary>When the game starts, the user will be welcommed with the Wordle banner :</summary>

<br>

![Display Wordle](assets/images/display_wordle.png)

</details>
<br>
<details>
<summary>The user can then decide if they want to read the rules or not :</summary>

<br>

![Wordle rules](assets/images/question_rules.png)

When y is pressed the rules will show.

![Wordle rules](assets/images/display_rules.png)

</details>
<br>
<details>
<summary>After the rules have been read or skipped, you can type in your name and country you're from :</summary>

<br>

![Name input](assets/images/question_name.png)

It will then validate the name input.

![Validating name input](assets/images/validating_name.png)

Then the country can be typed in.

![Country input](assets/images/question_country.png)

It will then validate the name input.

![Validating country input](assets/images/validating_country.png)

It will then show a small welcome message with whatever name and country (in English) you chose.

![Welcome message](assets/images/hello_message.png)

</details>
<br>
<details>
<summary>The game then starts where you can start guessing the 5 letter word :</summary>

<br>

![Start of the game](assets/images/start_game.png)

The word you guess has corresponding emojis underneath. Where if a letter is not in the word chosen by the computer, it will show a red cross underneath that letter. If a letter is in the word but in the incorrect spot, it will show a red circle. And finally if a letter is in the word and also in the correct spot, it will show a green check mark underneath.

![Word used with corresponding emojis](assets/images/guess_emoji.png)

</details>
<br>
<details>
<summary>Guessing the correct word, will show a small message congratulating the user :</summary>

<br>

![Correct word is guessed](assets/images/word_correct.png)

</details>
<br>
<details>
<summary>When the incorrect word is guessed, it will show a small "You lost" message with the correct word :</summary>

<br>

![You lost message](assets/images/you_lost.png)

</details>
<br>
<details>
<summary>The user is then asked if they want to see the leaderboard :</summary>

<br>

![Question for seeing the leaderboard](assets/images/question_leaderboard.png)

When y is pressed the leaderboard will show.

![Leaderboard](assets/images/leaderboard.png)

</details>
<br>
<details>
<summary>After the leaderboard is shown, the user is asked if they want to play again :</summary>

<br>

![Question to play again](assets/images/question_play_again.png)

When y is pressed the game will start again, starting with the user input. When n is pressed the game will exit.

![Exiting game](assets/images/question_exit.png)

</details>
<br>
<details>
<summary>Error messages :</summary>

<br>

When anything other than alphabetical letters and or spaces are used, this error message will be shown.

![Error message for name input](assets/images/error_name.png)

When anything other than country names are used, this error message will pop up.

![Error message for country input](assets/images/error_country.png)

When anything other than a 5 letter real word is used, this message pops up.

![Error message for word input](assets/images/error_word.png)

Then after 2 seconds this line gets deleted, so you can see your previous guesses easier.

![Error message for word deleted](assets/images/error_word_deleted.png)

When the user presseer anything other than y or n in these y/n questions, this message will be shown.

![Error message for y or n input](assets/images/error_y_n.png)

</details>

<br>


# Future features

- I want to change the code around so that if you decide to play again. It will copy the last name and country used. So the user would only have to fill out the name and country once. Currently if I don't have it the way it is now, the game would only add the score which would make the spreadsheet out of sync.
- I want to change the emoji's to having the background of the letter in a different colour for better readability and flow.
- I want the add the alphabet. Were the letters background changes to either red or yellow, when the wrong letter or the letter was in the wrong spot gets guesssed.
- I want to add a feature where after finishing the game and seeing the leaderboard, you see the users score highlighted in the leaderboard. And if the the user scores outside the spectrum of the leaderboard, it will still show seperatly underneath.
- I would like to add a feature that tells the user if a word has already been used.

<br>


# Design

I wanted the colours to have an oldschool vibe to it, so it fits the vibe of a terminal game. I added some cute emojis that would fit with the style. And added a green line through all the "seperate" sections in the game

![colour pallate](assets/images/colour_design.png)

![Display Wordle](assets/images/display_wordle.png)

![Wordle rules](assets/images/display_rules.png)

<br>


# Technologies used

- This project is written in Python
- [ChatGPT](https://chat.openai.com/) helped me with articulating myself better in the readme introduction.
- [Github](https://github.com/) was used to create a repository with the help of The Code Institute template.
- [Heroku](https://heroku.com/) was used to deploy my game.
- [Visual Studio Code](https://code.visualstudio.com/) is where I did all my coding.
- [HelpseoTools](https://helpseotools.com/text-tools/add-comma-online) helped me add a comma after every word in the countries file, for CSV to read the file properly.
- [TextFixer](https://www.textfixer.com/tools/remove-line-breaks.php) helped me get rid of the line breaks in my countries list, for CSV to read the file properly.
- [Favicon](https://favicon.io/) was used to create a unique favicon for the game.
- [Coolers](https://coolors.co/) was used to create a colour pallate.
- [Gif](https://ezgif.com/) was used to create a gif for my README.
- [emoji](https://emojipedia.org/) is where I got my emojis from.


## Lucid Flowchart

<details>
<summary>LucidChart was used to create a flow chart for planning my Python project.</summary>

<br>

[LucidChart](https://www.lucidchart.com/pages/)

![Flow Chart](assets/images/flow_chart.png)
</details>

<br>


## Google Sheets

<details>
<summary>Google Sheets was used to create a leaderboard. After finishing the game, the leaderboard will be updated and the user has a choice to see if they want to see the leaderboard top 10 lowest guesses.</summary>

<br>

[Google Sheets](https://www.google.com/sheets/about/)

![Google Sheets](assets/images/google_sheets.png)
</details>

<br>


## Libraries

I know I could use a library for my country list and word list however I wanted to show that I know how to also import from my own folders and also import data from a csv file and a txt file. So I import a few different ways

I got my libraries from different websites from the Code Institure project called Love Sandwiches :
- [<b>gspread</b>](https://docs.gspread.org/en/v5.10.0/) : The Code Institute helped me learn about that gspread is needed for connecting my Google Sheets to my python code.
- [<b>sys</b>](https://codedamn.com/news/python/exit-python-program-from-terminal) : I used the sys.exit() for when the user wants to exit the game.
- [<b>Rich</b>](https://rich.readthedocs.io/en/latest/introduction.html#installation) : I used the pannelling for the start page with Rich. Rich is also used to set the console width. And rprint() was used to print colourfull messages.
- [<b>Random</b>](https://www.geeksforgeeks.org/python-random-module/) : I used the Random import to randomize the word chosen by the computer.
- [<b>Credentials</b>](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) : The Code Institute helped me learn about credentials and that I needed them for my Google Sheets, which is used for my leaderboard list.
- [Time](https://docs.python.org/3/library/time.html) : Was needed for deleting the wordle error message after 2 seconds. 

<br>


# Testing

I did extensive testing to make sure my code has no bugs. As you can see in the [features](#features) - errors section, every incorrect input has it's own error message. Everything in my code works as it should :

<details>
<summary>Main Python</summary>

| Test | Result   |
| ---------- | -------- |
| Random import | &#10004; |
| Sys import | &#10004; |
| Time import | &#10004; |
| Gspread import | &#10004; |
| Rich import | &#10004; |
| Credentials | &#10004; |
| The Google spreadsheet called "leaderboard" is connected to the run.py file | &#10004; |
| Validations file | &#10004; |
| Game runs in Heroku | &#10004; |
| Game runs in VS Code | &#10004; |
| Game uploaded to GitHub| &#10004; |
| All internal files are read and opened correctly | &#10004; |
| All parameters work correctly | &#10004; |
| Game starts with the main function | &#10004; |
| Game runs in a loop until "n" is pressed in the play_again question | &#10004; |

</details>
<br>
<details>
<summary>Terminal designs</summary>

| Test | Result   |
| ---------- | -------- |
| The Wordle banner shows up undistorted | &#10004; |
| All ruler lines that split up the different "sections" of the game are shown | &#10004; |
| Message inside ruler lines are red and show different text | &#10004; |
| The rules get printed out without any distortion | &#10004; |
| All emojis show correctly | &#10004; |
| The pannels in the leaderboard show up undistorted | &#10004; |
| "You won" message shows with a green background after game is won | &#10004; |
| "You lost" message shows with a red background and the correct word after game is lost | &#10004; |
| The leaderboard shows up undistorted | &#10004; |
| Leaderboard is shown with name, country and score of the top 10 lowest guesses | &#10004; |

</details>
<br>
<details>
<summary>User Input</summary>

| Test | Result   |
| ---------- | -------- |
| The user can type their name in the name input | &#10004; |
| A "checking if input is correct" message will show | &#10004; |
| The user can type in the country they're from in the country input | &#10004; |
| A "checking if input is correct" message will show | &#10004; |
| A "Hello user from country" message will show | &#10004; |
| User name and country gets parsed into the play_wordle function | &#10004; |
| The user can type either "y" or "n" in the y/n questions | &#10004; |
| The user can type a 5 letter word in the wordle game| &#10004; |

</details>
<br>
<details>
<summary>Questions</summary>

| Test | Result   |
| ---------- | -------- |
| The question is asked if the user wants to see the rules | &#10004; |
| If "y" is pressed it will show the rules | &#10004; |
| When "n" is pressed, the rules will be skipped and show the user name input | &#10004; |
| The question is asked if the user wants to see the leaderboard | &#10004; |
| If "y" is pressed it will show the leaderboard | &#10004; |
| When "n" is pressed, it will show the "play again" question | &#10004; |
| The question is asked if the user wants to play the game again | &#10004; |
| If "y" is pressed it will show the user name input again | &#10004; |
| When "n" is pressed, the game will exit | &#10004; |

</details>
<br>
<details>
<summary>Wordle game</summary>

| Test | Result   |
| ---------- | -------- |
| Computer chooses random word from words list | &#10004; |
| The word the user chose gets shown again but spaced out in a new line | &#10004; |
| Underneath that shows the corresponding emojis, so they line up with the input word | &#10004; |
| User can see on which number of guesses they are | &#10004; |
| Score gets 1 extra point after every guess | &#10004; |
| If the correct word gets guessed by the user, it will finish the game | &#10004; |
| If the user can't guess the correct word in the 6 tries, the game will finish| &#10004; |
| After game is won or lost, the leaderboard will be updated with name, country and score of user| &#10004; |

</details>
<br>
<details>
<summary>Errors</summary>

| Test | Result   |
| ---------- | -------- |
| In the y/n questions, if anything other than y, Y, n or N is typed, an error message will be shown | &#10004; |
| when name input is anything other than spaces and alphabetical letters, an error pops up | &#10004; |
| When name input is less than 2 letters, a differenterror pops up | &#10004; |
| When country input is not in the countries list, it will show an error | &#10004; |
| When word input is not in the all_words list, it will show an error | &#10004; |
| The error message will then be deleted for better visuals | &#10004; |
| When an incorrect file in the read_file funtion is chosen, it will throw an error | &#10004; |

</details>


## HTML validation

<details>
<summary>The HTML validator came back without any issues. I used [this website](https://validator.w3.org/) to test my code.</summary>

<br>

![HTML validation](assets/images/html_validator.png)

</details>


## Python validation

<details>
<summary>The first time I put my run.py file through [The Code institutes Python linter](https://pep8ci.herokuapp.com/), the code came up with some minor isseus. I had indented incorrectly in the original panel display for the wordle banner. I first fixed this issue then later deleted this panel for a cleaner look. After fixing these minor issues the code came back without issues. My validation file came back with no issues.</summary>

<br>

![Python Linter](assets/images/python_linter_1.png)\
![Python Linter](assets/images/python_linter_2.png)\
![Python Linter](assets/images/python_linter_3.png)\
![Python Linter](assets/images/python_linter_4.png)

</details>

<br>


# Bug fixes

- When I ran the game after adding a validation for the word input, it kept going to the error that I wasn't using a real word. I started trouble shooting and found that I was comparing the user input with my english list. However my english list was in lowercase and my input I wanted the word to be in uppercase. So I changes the words file so that it returned in uppercase.
- I noticed that using country names that contained a space weren't working. I ended up changing the file to a csv file so that fixed it.
- I noticed that some of the words in the words file were names and also words that noone will know. So I went through the list to delete them.
- The leaderboard wasn't updating properly. I had the code written that you enter you name and country once and then the guesses will update after you finish playing the game. However when you wanted to play again only the leaderboard guesses would update and the rows would become out of sync. I fixed it by changing the code around that you fill in your name and country every time.
- There was an issue with the score adding a point even if the wrong word was used. I had placed the score "+= 1" code in the wrong spot.
- When I deployed my repo for the first time it came up with this error :
    * ERROR: Could not find a version that satisfies the requirement pywin32==306 (from versions: none)
    * ERROR: No matching distribution found for pywin32==306<br>
I googled it online and [this forum](https://stackoverflow.com/questions/50026190/heroku-fails-to-install-pywin32-library) told me to just delete "pywin32==306" from my requirements file.
- My Favicon wasn't working because I forgot to set up the correct path to the file.
- When the user entered their name and country it would update that data in the spreadsheet, however if the user then closes the game or there's an error, the spreadsheet would be out of sync. Because the score was only updating after finishing the game. I added parameters to the get_user_input function and added them to the play_wordle function.
- My y and n questions were closing the program after typing in the wrong input. I had forgotten to make these questions a while loop.
- When the user would type in the country input, every letter combo that is in the countries file would work for country validation. I had forgotten to make the country input a string, to fix this issue.

<b>I have not noticed any existing bugs.</b>

<br>


# Deployment

## Heroku deployment

To deploy Your App to Heroku, you have to :
- Create a Heroku account.
- From the dashboard select create new app.
- Enter a name for your app, it needs to be unique, and select your region then press create app.
- Select settings at the top of your app page.
- Press reveal config vars.
- If the user is using google sheets in their project, you'll have to name your credentials file in the key input and copy and paste that credential file in the value input.
- Also add PORT in key input and 8000 as value input.
- Scroll down and press the add buildpack button.
- From here press the Python icon and then the add buildpack button.
- Add another builpack and press the Nodejs icon this time and then press add buildpack button again.
- Scroll back up and select Deploy at the top of your app page.
- Choose your deployment method, when choosing Github, you will have to connect to your account.
- Then choose which repo you want to deploy and connect to it.
- Choose if you want to deploy automatic or manual, and press deploy.

## Github deployment

To fork this repository on Github, you have to :
  - Go to my [GitHub repository called PP3](https://github.com/ObiWanBonobi/PP3).
  - In the top-right corner of the page, click Fork.
  - Under "Owner," select the dropdown menu and click an owner for the forked repository.
  - By default, forks are named the same as their upstream repositories. Optionally, to further distinguish your fork, in the "Repository name" field, type a name.
  - Click Create fork.

To clone this repository, you have to :
  - Go to my [GitHub repository called PP3](https://github.com/ObiWanBonobi/PP3).
  - Above the list of files, click  Code.
  - Copy the URL for the repository.
  - Open Git Bash.
  - Change the current working directory to the location where you want the cloned directory.
  - Type git clone, and then paste the URL you copied earlier.
  - Press Enter to create your local clone.

You can see deployed game [here](https://wordle-bo-abd372c9b403.herokuapp.com/).

<br>


# Credits

- <b>FlowChart</b> : I got some ideas for my flowchart from [Pedro Cristo's PP3](https://github.com/PedroCristo/portfolio_project_3).
- <b>English words</b> : I got the english 5 letter words from [The free dictionary](https://www.thefreedictionary.com/5-letter-words.htm).
- <b>All words</b> : I got my list of all english words from [Charles Reid's Github](https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt)
- <b>Countries list</b> : I got the list of all countries from [World o meters](https://www.worldometers.info/geography/alphabetical-list-of-countries/).
- <b>README</b> : I copied some of the Readme code from my previous projects [PP1](https://github.com/ObiWanBonobi/PP1/blob/main/README.md) and [PP2](https://github.com/ObiWanBonobi/PP2/tree/main). I also got some ideas from [Gary Dolan's readme](https://github.com/GaryDolan/ci-p3-pokemon-portfolio). I got my table code from the [Codecademy](https://www.codecademy.com/resources/docs/markdown/tables) website. I got my emojis from this [Github page](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).
- <b>Python code</b> : I got a better understanding about Python code from these forums, websites and people :
  * I learned more about python coding from this [Real Python wordle project](https://realpython.com/python-wordle-clone/) website.
  * I learned more about enumerate from the [Geeks for Geeks](https://www.geeksforgeeks.org/enumerate-in-python/) website.
  * I got help with a better understanding of Python from my brother in law [Steffen Bjerkenås](https://github.com/stebje). He told me I needed to change my words list and country list to a text and CSV files and move them into a seperate file for better readability.
  * [GeeksforGeeks.org](https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/) helped me with understanding how to get a random word from a text file.
  * I got my get_leaderboard function from [Pedro Cristo's](https://github.com/PedroCristo/portfolio_project_3/blob/main/run.py) project the hangmans game. I would've figured the code out myself, however I was running out of time and needed to finish the project on time.
  * I learned a lot from the Code Institutes project [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode).
  * I learned more about how to append a row from this [stackoverflow](https://stackoverflow.com/questions/68859429/how-to-append-data-in-a-googlesheet-using-python) forum.
  * [Quora](https://www.quora.com/I%E2%80%99m-new-to-Python-how-can-I-write-a-yes-no-question) forum helped me with my y or n question, that wasn't working.
  * [Delete last line](https://linustechtips.com/topic/1257798-delete-last-line-in-console-python-3/) function was found on the linustechtips website.

- <b>Most of my credit goes to the Code Institute program where I made notes on every section and got most of my ideas and code from there.</b>
