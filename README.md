# Wordle

[Click on this link to visit the Github page](https://obiwanbonobi.github.io/PP3/)

[Click on this link to play the game on Heroku]()

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
- [Testing](#testing)
    * [Python validation](#python-validation)
    * [Lighthouse test](#lighthouse-test)
    * [Testing on devices and browsers](#testing-on-devices-and-browsers)
- [Bug fixes](#bug-fixes)
- [Deployment](#deployment)
    * [Github deployment](#github-deployment)
    * [Heroku deployment](#heroku-deployment)
- [Credits](#credits)

<br>

# Introduction

 I'm thrilled to present my very own Python-based Wordle game that promises to challenge and entertain you in equal measure. Dive into the realm of word-guessing, where you'll be tasked with unraveling a hidden five-letter word through strategic deduction and clever guessing.

## User experience

The user experience in my Wordle game has been meticulously crafted to ensure both enjoyment and ease of play. 

## My vision for the game

<br>

# Features

<br>

# Future features

- I want to change the code around so that the guesses get updated if you decide to play again. And it will copy the last name and country used. So the user would only have to fill out the name and country once.
- I want to change the emoji's to having the background of the letter in a different colour for better readability and flow. 

<br>

# Design

## Colour scheme

<br>

# Technologies used

## Lucid Flowchart

<br>

# Testing

## Python validation

## Lighthouse test

## Testing on devices and browsers

<br>

# Bug fixes

- When I ran the game after adding a validation for the word input, it kept going to the error that I wasn't using a real word. I started trouble shooting and found that I was comparing the user input with my english list. However my english list was in lowercase and my input I wanted the word to be in uppercase. So I changes the words file so that it returned in uppercase.
- I noticed that using country names that contained a space weren't working. I ended up changing the file to a csv file so that fixed it.
- I noticed that some of the words in the words file were names and also words that noone will know. So I went through the list to delete them.
- The leaderboard wasn't updating properly. I had the code written that you enter you name and country once and then the guesses will update after you finish playing the game. However when you wanted to play again only the leaderboard guesses would update and the rows would become out of sync. I fixed it by changing the code around that you fill in your name and country every time.

<br>

# Deployment

## Heroku deployment

To deploy Your App to Heroku, you have to :

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

You can see deployed game [here]().

<br>

# Credits

- <b>FlowChart</b> : I got some ideas for my flowchart from [this project](https://github.com/PedroCristo/portfolio_project_3) made by Pedro Cristo.
- <b>Emoji</b> : I got my emojis from [Emojipedia](https://emojipedia.org/).
- <b>ChatGPT</b> : ChatGPT helped me with articulating myself better in the readme introduction.
- <b>English words</b> : I got the english 5 letter words from [The free dictionary](https://www.thefreedictionary.com/5-letter-words.htm).
- <b>All words</b> : I got my list of all english words from a [GitHub account](https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt)
- <b>Countries list</b> : I got the list of all countries from [World o meters](https://www.worldometers.info/geography/alphabetical-list-of-countries/).
- <b>Python code</b> : I got a better understanding about Python code from these forums, websites and people :
  * [Enumerate()](https://www.geeksforgeeks.org/enumerate-in-python/)
  * I got help with a better understanding of Python from my brother in law [Steffen Bjerkenås](https://github.com/stebje). He told me I needed to change my words list and country list to a text and CSV files and move them into a seperate file for better readability.
  * [GeeksforGeeks.org](https://www.geeksforgeeks.org/pulling-a-random-word-or-string-from-a-line-in-a-text-file-in-python/) helped me with understanding how to get a random word from a text file.
  * [HelpseoTools](https://helpseotools.com/text-tools/add-comma-online) helped me add a comma after every word in the countries file, for CSV to read the file properly.
  * [TextFixer](https://www.textfixer.com/tools/remove-line-breaks.php) helped me get rid of the line breaks in my countries list, for CSV to read the file properly.
  * I got my get_leaderboard function from [Pedro Cristo's](https://github.com/PedroCristo/portfolio_project_3/blob/main/run.py) project the hangmans game. I would've figured the code out myself, however I was running out of time and needed to finish the project on time.
- <b>Python Library</b> : 
  * I got my colours from the [Rich library](https://rich.readthedocs.io/en/latest/introduction.html#installation).
  * I got my ASCII terminal banner from [Naufalardhani website](https://naufalardhani.medium.com/how-to-create-ascii-text-banner-for-command-line-project-85e75dc02b07).
  * I got my exit code from the [codedamn website](https://codedamn.com/news/python/exit-python-program-from-terminal).
